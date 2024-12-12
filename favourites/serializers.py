from rest_framework import serializers
from django.db import IntegrityError
from .models import Favourite


class FavouriteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Favourite model.

    Fields:
    - `id`: The unique identifier for each favourite instance.
    - `owner`: The username of the user who favourited the post (read-only).
    - `post`: The post that the favourite is associated with.
    - `created_at`: The timestamp of when the favourite was created.

    Methods:
    - `create`: Custom create method that catches `IntegrityError` exceptions
      to enforce the unique constraint on the combination of `owner` & `post`.
      Raises a `ValidationError` with a 'possible duplicate' message if a
      duplicate favourite is attempted.
    This serializer ensures that a user cannot favourite the
    same post more than once.
    """

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Favourite
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
