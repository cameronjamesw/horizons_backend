from rest_framework import status, generics
from .models import Profile
from .serializers import ProfileSerializer
from horizons_backend.permissions import IsOwnerOrReadOnly

# Create your views here.

class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()