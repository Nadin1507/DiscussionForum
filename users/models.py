from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    title = models.CharField(max_length=300)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


