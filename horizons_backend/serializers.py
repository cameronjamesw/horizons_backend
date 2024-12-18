from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth.models import User
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """
        Serializer for the current user, extending the default
        UserDetailsSerializer to include additional fields for
        the user's profile ID and profile image URL.

        Fields:
        - profile_id: Read-only field for the associated profile's ID.
        - profile_image: Read-only field for the URL of the
        associated profile's image.
    """
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')
    is_admin = serializers.SerializerMethodField()

    def get_is_admin(request, obj):
        """
        Determine if the current user is an admin
        """
        superusers = User.objects.filter(is_superuser=True)
        if obj in superusers:
            return True
        return False

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image', 'is_admin',
        )
