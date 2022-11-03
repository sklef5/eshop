from product.models import CategoryModel, ProductModel, ProductImagesModel, CategoryImagesModel
from product.serializers import CategorySerializer, ProductSerializer, ProductImageSerializer, CategoryImageSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user.is_staff)
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user.is_staff
        )


class CategoryListApiView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()
    permission_classes = [IsAdminOrReadOnly]

class CategoryRUDApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()
    permission_classes = [IsAdminOrReadOnly]

class ProductListApiView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()
    permission_classes = [IsAdminOrReadOnly]

class ProductRUDApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()
    permission_classes = [IsAdminOrReadOnly]

class ProductImgListAiView(ListCreateAPIView):
    serializer_class = ProductImageSerializer
    queryset = ProductImagesModel.objects.all()
    permission_classes = [IsAdminOrReadOnly]

class ProductImgRUDAiView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductImageSerializer
    queryset = ProductImagesModel.objects.all()
    permission_classes = [IsAdminOrReadOnly]

class CategoryImgListAiView(ListCreateAPIView):
    serializer_class = CategoryImageSerializer
    queryset = CategoryImagesModel.objects.all()
    permission_classes = [IsAdminOrReadOnly]

class CategoryImgRUDAiView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryImageSerializer
    queryset = CategoryImagesModel.objects.all()
    permission_classes = [IsAdminOrReadOnly]

