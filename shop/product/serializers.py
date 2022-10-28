from rest_framework import serializers

from cart.serializer import CartItemSerializer, OrderItemSerializer
from product.models import CategoryModel, ProductModel, ProductImagesModel, CategoryImagesModel


class CategoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryImagesModel
        fields = ['name', 'created_at', 'category', 'locate']

    def create(self, validated_data):
        return CategoryImagesModel.objects.create(**validated_data)

    def update(self, instance:CategoryImagesModel, validated_data):
        instance.name = validated_data['name']
        instance.locate=validated_data['locate']
        instance.category=validated_data['category']
        instance.created_at = validated_data.get("created_at", "")
        instance.save()
        return instance


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImagesModel
        fields = ['name', 'created_at', 'product', 'locate']

    def create(self, validated_data):
        return ProductImagesModel.objects.create(**validated_data)

    def update(self, instance:ProductImagesModel, validated_data):
        instance.name=validated_data['name']
        instance.product=validated_data['product']
        instance.locate=validated_data['locate']
        instance.created_at = validated_data.get("created_at", "")
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['name', 'manufacturer', 'description', 'price', 'availability', 'currency', 'category']

    def create(self, validated_data):
        return ProductModel.objects.create(**validated_data)

    def update(self, instance:ProductModel, validated_data):
        instance.name=validated_data['name']
        instance.description=validated_data.get("description", "")
        instance.manufactorer = validated_data.get("manufactorer", "")
        instance.price = validated_data.get("price", "")
        instance.availability = validated_data.get("availability", "")
        instance.currency = validated_data.get("currency", "")
        instance.category=validated_data['category']
        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['name',  'description', 'description', 'class_category']

    def create(self, validated_data):
        return CategoryModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data['name']
        instance.description=validated_data.get('description', '')
        instance.class_category=validated_data['class_category']
        instance.save()
        return instance