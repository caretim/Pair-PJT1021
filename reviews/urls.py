from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("create/", views.create, name="create"),
    path("index/", views.index, name="index"),
    path("<int:review_pk>", views.detail, name="detail"),
    path("<int:review_pk>/update/", views.update, name="update"),
    path("<int:review_pk>/delete/", views.delete, name="delete"),
    path("<int:review_pk>/comments/", views.comments, name="comments"),
    path("<int:review_pk>/comments/<int:comment_pk>/delete/", views.comments_delete, name="comments_delete"),
    path("<int:game_pk>/pick_game/", views.pick_game, name="pick_game"),
    
]
