from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, generics, filters
from rest_framework.response import Response
from .models import Post
from category.models import Category
from .serialziers import PostSerializer
from horizons_backend.permissions import IsOwnerOrReadOnly

# Create your views here.

class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend
    ]

    filterset_fields = [
        # User Feed
        'owner__followed__owner__profile',

        # User Liked Posts
        'likes__owner__profile',

        # User Posts
        'owner__profile',

        # Posts by Category
        'category',

        # User Favourite Posts
        'favourites__owner__profile',
    ]

    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    search_fields = [
        'owner__username',
        'title',
        'category__name',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')