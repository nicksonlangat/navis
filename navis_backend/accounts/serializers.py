from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = [
                 "id", "email", "first_name",
                 "last_name", "is_superuser",
                 "role", "id_number",
                "phone_number", "kra_pin"
                ]

class UserRegisterSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = fields = ["email", "password", "first_name", "last_name", "role", "id_number", "phone_number", "kra_pin"]
            extra_kwargs = {"password": {"write_only": True}}

        def validate_password(self, value):
            validate_password(value)
            return value

        def create(self, validated_data):
            user = User(**validated_data)
            user.set_password(validated_data["password"])
            user.save()
            return user
