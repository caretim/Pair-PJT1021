from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class MakeUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username",)
        labels = {
            "title" : "제목",
            "content" : "내용",
            "game_name" : "게임",
            "member" : "인원",
        }