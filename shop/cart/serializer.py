from rest_framework import serializers
from cart.models import CartModel, CartItemModel, OrderModel, OrderItemModel, OrderReturnModel


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItemModel
        fields = ['product', 'cart', 'quantity', 'active']

    def create(self, validated_data):
        return CartItemModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.product=validated_data['product']
        instance.cart=validated_data['cart']
        instance.quantity=validated_data['quantity']
        instance.active=validated_data['active']
        instance.save()
        return instance


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fields = ['cart', 'date_added', 'client']

    def create(self, validated_data):
        return CartModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.cart = validated_data['cart']
        instance.client=validated_data['client']
        instance.date_added = validated_data.get("date_added", "")
        instance.save()
        return instance


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItemModel
        fields = ['order', 'price', 'quantity', 'product']

    def create(self, validated_data):
        return OrderItemModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.price = validated_data['price']
        instance.quantity = validated_data['quantity']
        instance.order=validated_data['order']
        instance.product=validated_data['product']
        instance.save()
        return instance


class OrderReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderReturnModel
        fields = ['date_added', 'date_up']

    def create(self, validated_data):
        return OrderReturnModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date_added = validated_data['date_added']
        instance.date_up = validated_data.get("date_up", "")
        instance.save()
        return instance


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ['date_added', 'status', 'orders', 'user']

    def create(self, validated_data):
        return OrderModel.objects.create(**validated_data)

    def update(self, instance:OrderModel, validated_data):
        instance.status = validated_data['status']
        instance.date_added = validated_data.get("date_added", "")
        instance.user=validated_data['user']
        instance.status=validated_data['status']
        instance.save()
        return instance
