from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.Serializer):
    """Сериализатор для модели User"""

    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор создания пользователя
    """

    class Meta:
        model = User
        fields = ["email", "password", "name", "telegram"]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
