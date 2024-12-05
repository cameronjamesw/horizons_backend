from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):

    def get_is_admin(self, obj):
        superusers = User.objects.filter(is_superuser=True)
        return obj.owner in superusers

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'post_count',
            'created_at',
        ]