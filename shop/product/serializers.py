from rest_framework import serializers
from product.models import CategoryModel, ProductModel, ProductImagesModel, CategoryImagesModel


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=38)
    class_category= serializers.IntegerField(required=True)
    description = serializers.CharField(required=False, validators=[])
    slug = serializers.SlugField(required=False, max_length=38)
    created_at = serializers.DateField(read_only=True, required=False)
    update_at = serializers.DateField(read_only=True, required=False)

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

class CategoryImageSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=38)
    created_at = serializers.DateField(read_only=True, required=False)
    category = serializers.SlugField(read_only=True)

    def create(self, validated_data):
        return CategoryImagesModel.objects.create(**validated_data)

    def update(self, instance:CategoryImagesModel, validated_data):
        instance.name = validated_data['name']
        instance.category = validated_data['category']
        instance.created_at = validated_data.get("created_at", "")

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=150)
    slug = serializers.SlugField(required=True, max_length=150)
    manufactorer = serializers.CharField(required=True, max_length=38)
    created_at = serializers.DateField(read_only=True, required=False)
    update_at = serializers.DateField(read_only=True, required=False)
    description = serializers.CharField(required=False)
    category = serializers.CharField(source='categorymodel', read_only=True)
    price = serializers.IntegerField(required=False)
    availability = serializers.IntegerField(required=False, default=0)
    currency =  serializers.CharField(max_length=38, default='UAH')

    def create(self, validated_data):
        return ProductModel.objects.create(**validated_data)

    def update(self, instance:ProductModel, validated_data):
        instance.name=validated_data['name']
        instance.slug=validated_data['slug']
        instance.category = validated_data['category']
        instance.description=validated_data.get("description", "")
        instance.manufactorer = validated_data['manufactorer']
        instance.created_at = validated_data.get("created_at", "")
        instance.update_at = validated_data.get("update_at", "")
        instance.price = validated_data.get("price", "")
        instance.availability = validated_data.get("availability", "")
        instance.currency = validated_data.get("currency", "")
        instance.save()
        return instance


class ProductImageSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    create_at = serializers.DateField(read_only=True, required=False)
    product = serializers.CharField(source='productmodel')

    def create(self, validated_data):
        return ProductImagesModel.objects.create(**validated_data)

    def update(self, instance:ProductImagesModel, validated_data):
        instance.name=validated_data['name']
        instance.product = validated_data['product']
        instance.created_at = validated_data.get("created_at", "")
