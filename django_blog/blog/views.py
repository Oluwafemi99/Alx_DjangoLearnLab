from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile

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
    template_name = 'blog/register.html'


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
