from django.db import models
from django.contrib.auth.models import User
from category.models import Category

# Create your models here.

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/', default='../default_image_phixuu',
        blank=True
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='post')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'