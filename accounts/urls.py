from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("<int:user_pk>/update/", views.update, name="update"),
    path("<int:user_pk>/delete/", views.delete, name="delete"),
    path("<int:user_pk>/realdelete/", views.realdelete, name="realdelete"),
    path("<int:user_pk>/user_detail/", views.user_detail, name="user_detail"),
    path("members/", views.index, name="index"),
]
