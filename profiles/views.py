from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from horizons_backend.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer

# Create your views here.


class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer

    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
        favourites_count=Count('owner__favourite', distinct=True),
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]

    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]

    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
        favourites_count=Count('owner__favourite', distinct=True),
    ).order_by('-created_at')
