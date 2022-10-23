from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class MakeUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "image",
        )


class ChangeUserForm(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()
        fields = ("image", "email")
