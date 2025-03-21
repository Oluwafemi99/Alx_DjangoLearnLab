from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from rest_framework import generics
from .models import Post, Comment
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm

# Create your views here.


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = '__all__'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


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
def comment_detail(request, post_id):
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


class CommentEditView(generics.UpdateAPIView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    feilds = 'content'
    template_name = 'comment_update.html'


class CommentDeleteView(generics.UpdateAPIView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    feilds = 'content'
    template_name = 'comment_delete.html'
