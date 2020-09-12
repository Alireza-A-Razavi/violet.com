from django.db import models
from django.contrib.auth.models import AbstractUser


GENDER_CHOICES = (
    ("male","male"),
    ("female","female"),
)


class User(AbstractUser):
    is_producer = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.username

class ProducerProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES)
    is_selling = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
