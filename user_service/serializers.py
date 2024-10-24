from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'role', 'phone_number')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            role=validated_data['role'],
            phone_number=validated_data.get('phone_number', '')
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    print("####################################$$$$$$$$serializer")
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        print("###########################",username)
        print("###########################",password)
        user = authenticate(username=username, password=password)
        print("################################",user)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid login credentials.")

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    def validate_new_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("New password must be at least 8 characters long.")
        return value
