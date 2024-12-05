from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post_count = models.IntegerField(default=0, editable=False)

    class Meta:
        ordering = ['post_count']

    def __str__(self):
        return f'{self.name}, contains {self.post_count} posts'