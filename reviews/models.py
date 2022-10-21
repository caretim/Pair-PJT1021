from random import choices
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

# Create your models here.
game = [(1, '덕몽어스'), (2, '리그 오브 레전드'), (3, '오버워치2'), 
        (4, '어몽어스'), (5, '로스트 아크'), (6, '메이플스토리'), (7, '폴가이즈')]

class Review(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    game_name = models.IntegerField(choices=game)
    member = models.IntegerField(validators=[MinValueValidator(1),
                                        MaxValueValidator(20)])
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.CharField(max_length=80)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)