from rest_framework import serializers
from .models import Post
from likes.models import Like
from favourites.models import Favourite


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model.
    Converts Post instances to and from JSON for API interactions,
    with validations and computed fields for user-specific details.
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()
    category_name = serializers.ReadOnlyField(source='category.name')
    favourite_id = serializers.SerializerMethodField()

    def validate_image(self, value):
        """
        Validates the uploaded image:
        - Ensures it is less than 2MB.
        - Confirms that height and width are within 4096px.
        """
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2Mb'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height largerv than 4096px'
            )
        return value

    def get_is_owner(self, obj):
        """
        Checks if the authenticated user is the owner of the post.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        """
        Retrieves the ID of the Like object if the authenticated user
        has liked the post; returns None otherwise.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def get_favourite_id(self, obj):
        """
        Retrieves the ID of the Favourite object if the authenticated user
        has favourited the post; returns None otherwise.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            favourite = Favourite.objects.filter(
                owner=user, post=obj
            ).first()
            return favourite.id if favourite else None
        return None

    class Meta:
        model = Post
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'created_at',
            'updated_at',
            'title',
            'content',
            'image',
            'category',
            'category_name',
            'like_id',
            'favourite_id',
            'comments_count',
            'likes_count',
        ]
