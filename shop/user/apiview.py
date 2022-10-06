from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView

from user.models import UserModel
from user.serializer import UserSerializer


class UserListApiView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

class UserRUDApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()



