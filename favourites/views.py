from django.shortcuts import render
from rest_framework import generics, permissions
from horizons_backend.permissions import IsOwnerOrReadOnly
from .models import Favourite
from .serializers import FavouriteSerializer

# Create your views here.

class FavouriteList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FavouriteSerializer
    queryset = Favourite.objects.all()