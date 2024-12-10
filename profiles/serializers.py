from rest_framework import serializers
from django.contrib.auth.models import User
from followers.models import Follower
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    is_admin = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()

    def get_is_admin(self, obj):
        superusers = User.objects.filter(is_superuser=True)
        return obj.owner in superusers

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
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
        ]