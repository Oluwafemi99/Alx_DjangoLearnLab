from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # Only include these fields in the form

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
