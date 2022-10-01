from rest_framework import serializers
from cart.models import CartModel, CartItemModel, OrderModel, OrderItemModel, OrderReturnModel

class CartSerializer(serializers.Serializer):
    cart = serializers.CharField(required=True, max_length=250)
    date_added= serializers.DateField(read_only=True, required=False)
    client = serializers.CharField(source='usermodel')

    def create(self, validated_data):
        return CartModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.cart = validated_data['cart']
        instance.client = validated_data['client']
        instance.date_added = validated_data.get("created_at", "")

class CartItemSerializer(serializers.Serializer):
    product = serializers.CharField(source='productmodel')
    cart = serializers.CharField(source='cartmodel')
    quantity = serializers.IntegerField()
    active = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return CartItemModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.product = validated_data['product']
        instance.cart = validated_data['cart']
        instance.quantity = validated_data.get("quantity", "")
        instance.active = validated_data.get("active", "")


class OrderSerializer(serializers.Serializer):
    date_added = serializers.DateField(read_only=True, required=False)
    user = serializers.CharField(source='usermodel')
    status = serializers.CharField()

    def create(self, validated_data):
        return OrderModel.objects.create(**validated_data)

    def update(self, instance:OrderModel, validated_data):
        instance.user = validated_data['user']
        instance.status = validated_data['status']
        instance.date_added = validated_data.get("date_added", "")


class OrderItemSerializer(serializers.Serializer):
    order = serializers.CharField(source='ordermodel')
    product = serializers.CharField(source='productmodel')
    price = serializers.IntegerField(required=True, )
    quantity = serializers.IntegerField(required=True, )

    def create(self, validated_data):
        return OrderItemModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.order = validated_data['order']
        instance.product = validated_data['product']
        instance.price = validated_data['price']
        instance.quantity = validated_data['quantity']


class OrderReturnSerializer(serializers.Serializer):
    order = serializers.CharField(source='OrderModel')
    date_added = serializers.DateField(read_only=True, required=False)
    date_up = serializers.DateField(read_only=True, required=False)

    def create(self, validated_data):
        return OrderReturnModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.order = validated_data['order']
        instance.date_added = validated_data['date_added']
        instance.date_up = validated_data.get("date_up", "")

