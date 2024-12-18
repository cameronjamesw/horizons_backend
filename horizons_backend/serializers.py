from dj_rest_auth.serializers import UserDetailsSerializer
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
    is_admin = serializers.ReadOnlyField(source="profile.is_admin")

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image', 'is_admin'
        )
