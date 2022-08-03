from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Freelancer(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="'profiles/", blank=True)
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return f"{self.id} | {self.name}"

class Business(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="'profiles/", blank=True)
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.id} | {self.name}"