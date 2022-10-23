from dataclasses import field
from django import forms
from .models import Review, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            "title",
            "header_tag",
            "game_name",
            "member",
            "content",
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
        labels = {
            "title": "제목",
            "content": "내용",
            "game_name": "게임",
            "member": "인원",
        }
