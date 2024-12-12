from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Favourite(models.Model):
    """
    Represents the option to 'favourite' a post, created by a specific user.

    Fields:
    - `owner`: A ForeignKey to the User model representing
    the user who favourited the post.
    - `post`: A ForeignKey to the Post model representing the post that has
    been favourited. Uses `related_name='favourites'`
    to easily access all favourites associated with a post.
    - `created_at`: A DateTimeField that stores the timestamp of when the
    favourite was created.

    Meta Options:
    - `ordering`: Orders favourites by `created_at` in descending order, so the
    latest favourites appear first.
    - `constraints`: Ensures a unique constraint on the `owner` and `post`
    fields so that each user can only favourite a specific post once.

    Methods:
    - `__str__`: Returns a readable string representation
    of the favourite instance, showing the username of the owner and the
    title of the favourited post.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='favourites', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner}, {self.post}'
