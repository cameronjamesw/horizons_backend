from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
        Represents a category instance, each categpry is tied to an
        owner through the User Model,
        Each category has a OneToMany relationship with the Post
        Model
    """
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name}'
