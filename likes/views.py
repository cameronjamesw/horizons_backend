from rest_framework import generics, permissions
from horizons_backend.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    """
    get:
    Returns a list of all likes. Accessible to any user (authenticated or not).

    post:
    Allows an authenticated user to create a like on a post.
    The 'owner' field is automatically set to the current logged-in user.

    Permissions:
    - Any user can view the list of likes.
    - Only authenticated users can create a like.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    get:
    Retrieve details of a specific like by its ID. Available to any user.

    delete:
    Allows the owner of the like to delete it by its ID.
    Permissions:
    - Only the owner of the like can delete it.
    - Read access is available to any user.

    Notes:
    - Uses custom permission class `IsOwnerOrReadOnly` to ensure only the
    like's owner can delete it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
