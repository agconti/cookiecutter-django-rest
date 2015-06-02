from rest_framework import generics

from .models import User
from .permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer


class UserView(generics.CreateAPIView, generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)
