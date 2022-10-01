from rest_framework import serializers
from cart.models import CartModel, CartItemModel, OrderModel, OrderItemModel, OrderReturnModel


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItemModel
        fields = ['quantity', 'active']

    def create(self, validated_data):
        return CartItemModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get("quantity", "")
        instance.active = validated_data.get("active", "")


class CartSerializer(serializers.ModelSerializer):
    carts = CartItemSerializer(many=True)
    class Meta:
        model = CartModel
        fields = ['cart', 'date_added', 'carts']

    def create(self, validated_data):
        return CartModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.cart = validated_data['cart']
        instance.date_added = validated_data.get("created_at", "")


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItemModel
        fields = ['price', 'quantity']

    def create(self, validated_data):
        return OrderItemModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.price = validated_data['price']
        instance.quantity = validated_data['quantity']


class OrderReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderReturnModel
        fields = ['date_added', 'date_up']

    def create(self, validated_data):
        return OrderReturnModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date_added = validated_data['date_added']
        instance.date_up = validated_data.get("date_up", "")


class OrderSerializer(serializers.ModelSerializer):
    orders = OrderItemSerializer(many=True)
    ordersret = OrderReturnSerializer(many=True)
    class Meta:
        model = OrderModel
        fields = ['date_added', 'status', 'orders']

    def create(self, validated_data):
        return OrderModel.objects.create(**validated_data)

    def update(self, instance:OrderModel, validated_data):
        instance.status = validated_data['status']
        instance.date_added = validated_data.get("date_added", "")

