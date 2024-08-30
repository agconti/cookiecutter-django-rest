from rest_framework import viewsets, mixins
from .models import User
from .permissions import IsUserOrCreatingAccountOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrCreatingAccountOrReadOnly,)

    def get_serialzier_class(self):
        is_creating_a_new_user = self.action == 'create'
        if is_creating_a_new_user:
            return CreateUserSerializer
        return self.serializer_class
