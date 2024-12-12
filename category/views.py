from django.db.models import Count
from rest_framework import generics, permissions, filters
from horizons_backend.permissions import IsAdminUserOrReadOnly
from .models import Category
from .serializers import CategorySerializer


class CategoryList(generics.ListCreateAPIView):
    """
    List the categories, or create a category if
    you are an admin user.
    """
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.annotate(
        posts_count=Count('post')
    ).order_by('-created_at')  # Orders categories by `created_at`

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter
    ]

    ordering_fields = [
        'posts_count',  # Orders categories based on post count
    ]

    search_fields = [
        'name',  # Search for categories by name
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves the details about a specific category

    Permission used is `IsAdminUser` - only admin users
    can retrieve, update and destroy category details
    """
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.annotate(
        posts_count=Count('post')
    ).order_by('-created_at')
