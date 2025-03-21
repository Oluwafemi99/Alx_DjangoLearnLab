from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile, Tag
from rest_framework import generics
from .models import Post, Comment
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm, CustomUserCreationForm
from django.db.models import Q

# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


# Access to only users with login details
@login_required
def profile_view(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        bio = request.POST.get("bio")

        if username and email:
            user.username = username
            user.email = email
            user.save()
            user_profile.bio = bio

            # Save profile picture only if provided
            if request.FILES.get("profile_picture"):
                user_profile.profile_picture = request.FILES.get("profile_picture")
            user_profile.save()

            messages.success(request, "Your profile has been updated successfully.")
            return redirect('profile')
        else:
            messages.error(request, "Username and Email are required.")

    return render(request, "profile.html", {
        "username": user.username,
        "email": user.email,
        "bio": user_profile.bio,
        "profile_picture": user_profile.profile_picture,
    })


class ListView(generics.ListAPIView):
    queryset = Post.objects.all()
    permission_classes = IsAuthenticated
    template_name = 'post_list.html'


class DetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    permission_classes = IsAuthenticated
    template_name = 'post_detail.html'


class CreateView(generics.CreateAPIView, LoginRequiredMixin):
    queryset = Post.objects.all()
    permission_classes = []
    template_name = 'post_create.html'


class UpdateView(generics.UpdateAPIView, LoginRequiredMixin, UserPassesTestMixin):
    queryset = Post.objects.all()
    permission_classes = []
    template_name = 'post_update.html'


class DeleteView(generics.DestroyAPIView, LoginRequiredMixin, UserPassesTestMixin):
    queryset = Post.objects.all()
    permission_classes = IsAuthenticated
    template_name = 'post_delete.html'


@login_required
def CommentCreateView(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()  # Retrieve all comments related to the post
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user  # Set the logged-in user as the author
            comment.post = post  # Associate the comment with the current post
            comment.save()
            return redirect('post_detail', post_id=post.id)

    return render(request, 'comment_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })


class CommentUpdateView(generics.UpdateAPIView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    feilds = 'content'
    template_name = 'comment_update.html'


class CommentDeleteView(generics.UpdateAPIView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    feilds = 'content'
    template_name = 'comment_delete.html'


class PostSearchView(generics.ListAPIView):
    model = Post
    template_name = 'search_results.html'
    context_object_name = 'results'  # Use 'results' to access the filtered posts in the template

    def get_queryset(self):
        query = self.request.GET.get('q', '')  # Get the search term from the query parameters
        queryset = Post.objects.all()  # Start with all posts
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |  # Case-insensitive search in the title
                Q(content__icontains=query) |  # Case-insensitive search in the content
                Q(tags__name__icontains=query)  # Search in tags (requires django-taggit)
            ).distinct()  # Ensure no duplicate results if multiple fields match
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')  # Pass the search term to the template
        return context


class PostByTagListView(generics.ListAPIView):
    model = Post
    template_name = 'posts_by_tag.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag_slug = self.kwargs['slug']
        tag = get_object_or_404(Tag, slug=tag_slug)
        return Post.objects.filter(tags__in=[tag]).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return context
