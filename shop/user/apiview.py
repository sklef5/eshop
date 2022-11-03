from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework import permissions
from user.models import UserModel
from user.serializer import UserSerializer

class IsAnonim(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_anonymous)

class isAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.username == request.user.username or request.user.is_staff:
            return True

class UserCreateApiView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [IsAnonim]

class UserListApiView(ListAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [permissions.IsAdminUser]

class UserRUDApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [isAuthor]




