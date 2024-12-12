from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from horizons_backend.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    API view to list all profiles.

    - Profiles are annotated with additional fields:
        - `posts_count`: The number of posts created by the profile owner.
        - `followers_count`: The number of users following the profile owner.
        - `following_count`: The number of users the profile owner is following
    - Profiles are ordered by their creation date (descending) by default.

    Filtering and ordering:
    - Filters:
        - Profiles followed by the current user:
        `owner__following__followed__profile`.
        - Profiles following the current user:
        `owner__followed__owner__profile`.
    - Ordering fields:
        - `posts_count`: Total posts by the profile owner.
        - `followers_count`: Total followers of the profile owner.
        - `following_count`: Total users the profile owner follows.
        - `owner__following__created_at`: Date of following activity.
        - `owner__followed__created_at`: Date of follower activity.
    """

    serializer_class = ProfileSerializer

    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
        favourites_count=Count('owner__favourite', distinct=True),
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,  # Enabled ordering by specified fields
        DjangoFilterBackend  # Enabled filtering using DjangoFilterBackend
    ]

    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]

    filterset_fields = [
        # Filter profiles followed by the current user
        'owner__following__followed__profile',

        # Filter profiles following the current user
        'owner__followed__owner__profile',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    API view to retrieve or update a single profile.

    - Only the owner of the profile can update it.
    - The profile includes annotations for additional fields:
        - `posts_count`: The number of posts created by the profile owner.
        - `followers_count`: The number of users following the profile owner.
        - `following_count`: The number of users the profile owner is following
    - Profiles are ordered by their creation date (descending) by default.

    Permissions:
    - Read-only access is allowed for all users.
    - Update access is restricted to the owner of the profile.
    """

    serializer_class = ProfileSerializer

    # Custom permission to restrict updates to the owner
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
        favourites_count=Count('owner__favourite', distinct=True),
    ).order_by('-created_at')  # Default ordering by creation date
