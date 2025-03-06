from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PasswordReset

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("No user with this email found.")
        return value

class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, min_length=5)
    confirm_password = serializers.CharField(write_only=True, min_length=5)

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        return data
