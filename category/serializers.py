from django.db import IntegrityError
from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category model.

    Fields:
        - `id` (int): Unique identifier for the comment, read-only.
        - `owner` (str): Username of the category owner, read-only.
        - `name` (str): The name of the category instance
        - `created_at` (str): Human-readable timestamp of when the comment was
        created, read-only.
        - `posts_count` (int): Lists the amount of posts tied to a category
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    posts_count = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = [
            'id',
            'owner',
            'name',
            'created_at',
            'posts_count',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
