from django.shortcuts import render
from rest_framework import generics, permissions
from horizons_backend.permissions import IsOwnerOrReadOnly
from .models import Favourite
from .serializers import FavouriteSerializer


class FavouriteList(generics.ListCreateAPIView):
    """
    get:
    Returns a list of all favourited posts. Accessible to any
    user (authenticated or not).

    post:
    Allows an authenticated user to create an instance of a favourited post.
    The 'owner' field is automatically set to the current logged-in user.

    Permissions:
    - Any user can view the list of favourite instances.
    - Only authenticated users can favourite a post.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FavouriteSerializer
    queryset = Favourite.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FavouriteDetail(generics.RetrieveDestroyAPIView):
    """
    get:
    Retrieve details of a specific favourite by its ID. Available to any user.

    delete:
    Allows the owner of the favourite to delete it by its ID.
    Permissions:
    - Only the owner of the favourited post can delete it.
    - Read access is available to any user.

    Notes:
    - Uses custom permission class `IsOwnerOrReadOnly` to ensure only the
    favourite's owner can delete it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FavouriteSerializer
    queryset = Favourite.objects.all()
