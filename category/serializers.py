from rest_framework import serializers
from django.db import IntegrityError
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
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