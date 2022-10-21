from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    image = ProcessedImageField(blank = True,
    processors=[ResizeToFill(200, 300)],
    format = 'JPEG',
    options={'quality' : 90},)