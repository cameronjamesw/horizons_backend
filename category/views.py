from django.db.models import Count
from rest_framework import generics, permissions, filters
from horizons_backend.permissions import IsAdminUserOrReadOnly
from .models import Category
from .serializers import CategorySerializer

# Create your views here.


class CategoryList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.annotate(
        posts_count=Count('post')
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter
    ]

    ordering_fields = [
        'posts_count',
    ]

    search_fields = [
        'name'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.annotate(
        posts_count=Count('post')
    ).order_by('-created_at')
