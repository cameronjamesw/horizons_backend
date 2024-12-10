from django.http import Http404
from django.shortcuts import render
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
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
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()