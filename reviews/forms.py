from dataclasses import field
from django import forms
from .models import Review, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("title", "game_name", "member", "content", )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content", )