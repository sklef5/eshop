from rest_framework import serializers

from cart.serializer import CartSerializer, OrderSerializer
from user.models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = [ 'password',  'username',   'age', 'cash', 'first_name', 'last_name', 'email' ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserModel(
            email=validated_data['email'],
            username=validated_data['username'],
            age=validated_data['age'],
            cash=validated_data.get('cash', '**'),
            last_name=validated_data.get('last_name', '**'),
            first_name=validated_data.get('first_name', '**')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.slug = validated_data.get["slug"]
        instance.cash = validated_data['cash']
        instance.email = validated_data.get("email", "")
        instance.password = validated_data['password']
        instance.age = validated_data.get("age", "")
        instance.first_name = validated_data.get("first_name", "")
        instance.last_name = validated_data.get("last_name", "")
