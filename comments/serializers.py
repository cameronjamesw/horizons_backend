from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for Comment model.

    Fields:
        - `owner` (str): Username of the comment owner, read-only.
        - `is_owner` (bool): Indicates if the logged-in user is the owner of
        the comment.
        - `profile_id` (int): ID of the owner's profile, read-only.
        - `profile_image` (str): URL of the owner's profile image, read-only.
        - `created_at` (str): Human-readable timestamp of when the comment was
        created, read-only.
        - `updated_at` (str): Human-readable timestamp of the last update on
        the comment, read-only.
        - `content` (str): Content of the comment.
        - `post` (int): ID of the post the comment is associated with.

    Methods:
        - `get_is_owner`: Checks if the logged-in user is the owner of the
        comment.
        - `get_created_at`: Returns the created timestamp in a human-readable
        format.
        - `get_updated_at`: Returns the updated timestamp in a human-readable
        format.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Check if the logged-in user is the owner of the comment.

        Args:
            obj (Comment): The comment instance.

        Returns:
            bool: True if the logged-in user is the owner of the comment,
            False otherwise.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        """
        Get a human-readable representation of the comment's creation
        timestamp.

        Args:
            obj (Comment): The comment instance.

        Returns:
            str: Human-readable timestamp for when the comment was created.
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Get a human-readable representation of the comment's last update
        timestamp.

        Args:
            obj (Comment): The comment instance.

        Returns:
            str: Human-readable timestamp for when the comment was last
            updated.
        """
        return naturaltime(obj.updated_at)

    class Meta:
        model = Comment
        fields = [
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'created_at',
            'updated_at',
            'content',
            'post',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    post = serializers.ReadOnlyField(source='post.id')
