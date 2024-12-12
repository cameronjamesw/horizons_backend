from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, generics, filters
from rest_framework.response import Response
from .models import Post
from category.models import Category
from .serialziers import PostSerializer
from horizons_backend.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    """
    API view to list all posts or create a new post.
    - List all posts, with filtering, searching, and ordering options.
    - Authenticated users can create posts.
    """
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
        'likes_count',  # Order ny number of likes
        'comments_count',  # Order by number of comments
        'likes__created_at',  # Order by creation date of likes
    ]

    search_fields = [
        'owner__username',  # Search by username of the owner
        'title',  # Search by name of the tit;e
        'category__name',  # Search by category
    ]

    def perform_create(self, serializer):
        """
        Override perform_create to associate the post
        with the logged-in user.
        """
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a single post.
    - Only the owner of the post can edit or delete it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
