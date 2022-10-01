from rest_framework import serializers
from user.models import UserModel

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=15)
    slug = serializers.SlugField(max_length=15)
    age = serializers.IntegerField(required=False)
    cash = serializers.IntegerField(default=10000)
    first_name =serializers.CharField(max_length=50, required=False)
    last_name =serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=50, required=False)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'}, max_length=128)

    def create(self, validated_data):
        return UserModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.slug = validated_data.get("slug", "")
        instance.cash = validated_data['cash']
        instance.email = validated_data.get("email", "")
        instance.password = validated_data['password']
        instance.age = validated_data.get("age", "")
        instance.first_name = validated_data.get("first_name", "")
        instance.last_name = validated_data.get("last_name", "")
