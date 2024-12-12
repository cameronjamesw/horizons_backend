from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Like(models.Model):
    """
    Represents a 'like' on a post, created by a specific user.

    Fields:
    - `owner`: A ForeignKey to the User model representing the user who liked
    the post.
    - `post`: A ForeignKey to the Post model representing the post that has
    been liked. Uses `related_name='likes'` to easily access all likes
    associated with a post.
    - `created_at`: A DateTimeField that stores the timestamp of when the
    like was created.

    Meta Options:
    - `ordering`: Orders likes by `created_at` in descending order, so the
    latest likes appear first.
    - `constraints`: Ensures a unique constraint on the `owner` and `post`
    fields so that each user can only like a specific post once.

    Methods:
    - `__str__`: Returns a readable string representation of the like instance,
    showing the username
      of the owner and the title of the liked post.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return {self.owner}, {self.post}
