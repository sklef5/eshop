from rest_framework import serializers
from cart.serializer import CartItemSerializer, OrderItemSerializer
from product.models import CategoryModel, ProductModel, ProductImagesModel, CategoryImagesModel


class CategoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryImagesModel
        fields = ['name', 'created_at']

    def create(self, validated_data):
        return CategoryImagesModel.objects.create(**validated_data)

    def update(self, instance:CategoryImagesModel, validated_data):
        instance.name = validated_data['name']
        instance.created_at = validated_data.get("created_at", "")


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImagesModel
        fields = ['name', 'created_at']

    def create(self, validated_data):
        return ProductImagesModel.objects.create(**validated_data)

    def update(self, instance:ProductImagesModel, validated_data):
        instance.name=validated_data['name']
        instance.created_at = validated_data.get("created_at", "")


class ProductSerializer(serializers.Serializer):
    products = CartItemSerializer(many=True)
    productsord = OrderItemSerializer(many=True)
    prodimg = ProductImageSerializer(many=True)
    class Meta:
        model = ProductModel
        fields = ['name', 'productimg', 'products', 'productsord', 'slug', 'manufacturer', 'created_at', 'update_at', 'description', 'price', 'availability', 'currency', ]

    def create(self, validated_data):
        return ProductModel.objects.create(**validated_data)

    def update(self, instance:ProductModel, validated_data):
        instance.name=validated_data['name']
        instance.slug=validated_data['slug']
        instance.description=validated_data.get("description", "")
        instance.manufactorer = validated_data['manufactorer']
        instance.created_at = validated_data.get("created_at", "")
        instance.update_at = validated_data.get("update_at", "")
        instance.price = validated_data.get("price", "")
        instance.availability = validated_data.get("availability", "")
        instance.currency = validated_data.get("currency", "")
        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):
    categories = ProductSerializer(many=True)
    catimg = CategoryImageSerializer(many=True)
    class Meta:
        model = CategoryModel
        fields = ['name', 'slug', 'class_category', 'created_at', 'update_at', 'description', 'categories']

    def create(self, validated_data):
        return CategoryModel.objects.create(**validated_data)

    def update(self, instance:CategoryModel, validated_data):
        instance.name=validated_data['name']
        instance.class_category=validated_data['class_category']
        instance.description=validated_data.get("description", "")
        instance.slug = validated_data['slug']
        instance.created_at = validated_data.get("created_at", "")
        instance.update_at = validated_data.get("update_at", "")
        instance.save()
        return instance
