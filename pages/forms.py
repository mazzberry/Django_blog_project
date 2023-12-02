from django import forms
from .models import Post


class newPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'author',
            'status'
        ]