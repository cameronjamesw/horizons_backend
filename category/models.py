from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    post_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['post_count']

    def __str__(self):
        return f'{self.name}'