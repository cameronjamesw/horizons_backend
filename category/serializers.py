from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    is_admin = serializers.SerializerMethodField()

    def get_is_admin(self, obj):
        superusers = User.objects.filter(is_superuser=True)
        return obj.owner in superusers