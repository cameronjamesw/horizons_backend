from django.contrib.auth.models import User
from rest_framework import serializers
from followers.models import Follower
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    ProfileSerializer serializes the Profile model and provides additional
    fields for user interaction.
    Fields:
    - `owner`: A read-only field that displays the username of the profile
      owner. It's derived from the 'owner.username' attribute of the Profile
      model.
    - `is_owner`: A boolean field that indicates whether the current request
      user is the owner of the profile. It is determined using the
      `get_is_owner` method.
    - `is_admin` : A boolean field that indicates whether the current user
      in an admin. It is determined using the `get_is_admin` method.
    - `following_id`: Shows the ID of the following relationship if the current
      user follows the profile owner; otherwise, it returns `None`.
    - `posts_count` : This field determines the amount of posts
    the current user has.
    - `followers_count` : This field determines the amount of followers the
      current user has.
    - `following_count` : This field determines the amount of users
    the current user is following.
    - `favourites_count` : This field determines the amount of favourited posts
      the current user has.
    Methods:
    - `get_is_owner`: Compares the current request user with the profile owner
      and returns `True` if they match; otherwise, `False`.
    - `get_following_id`: Retrieves the ID of the following relationship if it
      exists; otherwise, returns `None`.
    Meta:
    - `model`: The Profile model.
    - `fields`: Specifies which fields to include in the serialized output.
      These fields include `id`, `owner`, `created_at`, `updated_at`, `name`,
      `description`, `image`, `is_owner`, `following_id`, `posts_count`,
      `followers_count`, and `following_count`.
    """
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    is_admin = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    favourites_count = serializers.ReadOnlyField()

    def get_is_admin(self, obj):
        """
        Determine if the current user is an admin
        """
        superusers = User.objects.filter(is_superuser=True)
        return obj.owner in superusers

    def get_is_owner(self, obj):
        """
        Determine if the current user is the owner of the profile.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        """
        Retrieve the ID of the following relationship if it exists.
        Returns None if the user is not authenticated or not following.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'name',
            'island_name',
            'friend_code',
            'bio',
            'created_at',
            'updated_at',
            'image',
            'is_owner',
            'is_admin',
            'following_id',
            'posts_count',
            'followers_count',
            'following_count',
            'favourites_count',
        ]
