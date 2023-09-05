from rest_framework import serializers
from .models import User

class UserOutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = [
                 "id", "email", "first_name",
                 "last_name", "is_superuser"
                ]
