from django.urls import path
from . import views

app_name = "first_view"

urlpatterns = [
    path("", views.first, name="first"),
]