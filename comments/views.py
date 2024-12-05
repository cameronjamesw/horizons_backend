from django.shortcuts import render
from rest_framework import generics, permissions
from horizons_backend.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer

# Create your views here.

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [
        IsOwnerOrReadOnly
    ]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsOwnerOrReadOnly
    ]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()