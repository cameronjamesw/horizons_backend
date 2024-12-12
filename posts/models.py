from django.db import models
from django.contrib.auth.models import User
from category.models import Category

# Create your models here.
"""
    Post model representing an event created by a user.

    Attributes:
        owner (ForeignKey): The user who created the post.
        title (CharField): The title of the post
        content (Textfield): The content of the post
        created_at (DateTimeField): Timestamp when the post was created.
        updated_at (DateTimeField): Timestamp when the post was last updated.
        image (ImageField): Optional image for the event. Uploaded to
                            'images/' by default, with a fallback to a
                            default image ('../default_image_phixuu').
        category (ForeignKey): The category the post falls under.

    Meta:
        - Posts are ordered by creation time in descending order
        (`-created_at`).

    Methods:
        __str__: Returns a string representation of the post, displaying its
                 ID and title.
    """


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
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name='post')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
