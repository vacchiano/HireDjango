from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Role(models.Model):
    ROLE_CHOICES = [
        ('Part-time' , 'Part-time'),
        ('Full-time' , 'Full-time'),
        ('Contract' , 'Contract'),
    ]
    name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.name

class Level(models.Model):
    LEVEL_CHOICES = [
        ('Junior' , 'Junior'),
        ('Mid-level' , 'Mid'),
        ('Senior' , 'Senior'),
        ('Principal' , 'Principal'),
        ('C-level' , 'CTO'),
    ]
    name = models.CharField(max_length=50, choices=LEVEL_CHOICES, unique=True)

    def __str__(self):
        return self.name

class Freelancer(models.Model):

    STATUS_CHOICES = [
        ('active' , 'Active'),
        ('open' , 'Open'),
        ('interested' , 'Interested'),
        ('invisible' , 'Invisible'),
    ]

    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="freelancer")
    profile_pic = models.ImageField(upload_to="profiles/")
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    github = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    stackoverflow = models.URLField(max_length=200, blank=True)
    search_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='active')
    role_type = models.ManyToManyField("Role", blank=True, null=True)
    role_level = models.ManyToManyField("Level", blank=True, null=True)
    available_date = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    contact_email = models.EmailField(max_length=254, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.id} | {self.name}"

    class Meta:
        ordering = ['-id']

class Business(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="profiles/", blank=True)
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    website = models.URLField(max_length=200, blank=True)
    job_title = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.id} | {self.name}"