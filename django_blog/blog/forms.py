from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from taggit.forms import TagWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Only include these fields in the form
        widgets = {
            'tags': TagWidget(attrs={'placeholder': 'Add tags here'}),
        }

    def save(self, commit=True, user=None):
        """
        Override the save method to set the author automatically
        based on the logged-in user.
        """
        instance = super(PostForm, self).save(commit=False)
        if user is not None:
            instance.author = user
        if commit:
            instance.save()
        return instance


class CommentForm(forms.ModelForm):
    class meta:
        model = Comment
        feilds = "content"

    def clean_content(self):
        # Custom validation for content field
        content = self.cleaned_data.get('content')
        if not content or content.strip() == "":
            raise forms.ValidationError("Content cannot be empty.")
        if len(content) < 10:
            raise forms.ValidationError("Comment is too short. Please write at least 10 characters.")
        return content


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
