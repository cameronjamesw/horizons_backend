from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a user's profile in the system. Each profile is linked to a User
    via a one-to-one relationship.

    Attributes:
        owner (ForeignKey): A one-to-one relationship to the User model,
        representing the owner of the profile.
        created_at (DateTimeField): The timestamp when the profile was created.
        Automatically set on creation.
        updated_at (DateTimeField): The timestamp when the profile was last
        updated. Automatically updated.
        name (CharField): The user's name, which can be left blank.
        island_name (CharField): The user's island name
        friend_code (CharField): The user's friendcode
        bio (TextField): This allows the user to has their own bio
        image (ImageField): The user's profile image. Defaults to a placeholder
        image if not provided.
    Meta:
        ordering: Orders profiles by creation date in descending order.

    Methods:
        __str__(): Returns a string representation of the profile,
        showing the owner's username.
    """

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, blank=True)
    island_name = models.CharField(max_length=50, blank=False)
    friend_code = models.CharField(max_length=12, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../leaf_lngcw0'
    )

    class Meta:
        ordering: ['-created_at']

    def __str__(self):
        """
        This dunder method returns a string of the
        user's username and island_name
        """
        return f"{self.owner} of {self.island_name}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Signal handler to automatically create a Profile instance whenever a
    new User is created.

    This function is connected to the Django `post_save` signal for the
    User model. It checks if a new User instance has been created and, if so,
    automatically generates a corresponding Profile instance with the User
    set as the owner.

    Args:
        sender (Model class): The model class that sends the signal
        (in this case, User).
        instance (Model instance): The instance of the model being saved
        created (bool): A boolean indicating whether a new record was created
        (True if a new User was created).
        **kwargs: Additional keyword arguments passed by the signal.

    Returns:
        None
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
