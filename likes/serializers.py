from django.db import IntegrityError
from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model.

    Fields:
    - `id`: The unique identifier for each like instance.
    - `owner`: The username of the user who liked the post (read-only).
    - `post`: The post that the like is associated with.
    - `created_at`: The timestamp of when the like was created.

    Methods:
    - `create`: Custom create method that catches `IntegrityError` exceptions
      to enforce the unique constraint on the combination of `owner` & `post`.
      Raises a `ValidationError` with a 'possible duplicate' message if a
      duplicate like is attempted.
    This serializer ensures that a user cannot like the same post more than
    once.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = [
            'id',
            'owner',
            'post',
            'created_at',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
