from product.models import CategoryModel, ProductModel, ProductImagesModel, CategoryImagesModel
from product.serializers import CategorySerializer, ProductSerializer, ProductImageSerializer, CategoryImageSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView


class CategoryListApiView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()

class CategoryRUDApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()

class ProductListApiView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()

class ProductRUDApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()

class ProductImgListAiView(ListCreateAPIView):
    serializer_class = ProductImageSerializer
    queryset = ProductImagesModel.objects.all()

class ProductImgRUDAiView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductImageSerializer
    queryset = ProductImagesModel.objects.all()

class CategoryImgListAiView(ListCreateAPIView):
    serializer_class = CategoryImageSerializer
    queryset = CategoryImagesModel.objects.all()

class CategoryImgRUDAiView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryImageSerializer
    queryset = CategoryImagesModel.objects.all()

