from tkinter import Widget
from django import forms
from .models import Review, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("title", "header_tag", "game_name", "member", "content", )
        labels = {
            "title" : "제목",
            "header_tag": "말머리",
            "content" : "내용",
            "game_name" : "게임",
            "member" : "인원",
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
        labels = {
            "content" : "",
        }
        widget = forms.TextInput(attrs={
                                 'placeholder': "댓글을 작성해주세요."
                                 })