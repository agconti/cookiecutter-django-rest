from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'auth_token', 'first_name', 'last_name',)
        read_only_fields = ('username', 'auth_token',)


class CreateUserSerializer(UserSerializer):

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        user = User.objects.create_user(**validated_data)
        return user

    class Meta(UserSerializer.Meta):
        fields = ('id', 'username', 'auth_token', 'first_name', 'last_name',
                  'password')
        write_only_fields = ('password',)
