from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers, status, exceptions
from rest_framework.views import APIView
from rest_framework.response import Response

from .services import get_tokens_for_user

from common.pagination import (
    LimitOffsetPagination,
    get_paginated_response,
)
from .models import User
from .selectors import user_list


class UserCreateApi(APIView):
    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ["email", "password", "first_name", "last_name"]
            extra_kwargs = {"password": {"write_only": True}}

        def validate_password(self, value):
            validate_password(value)
            return value

        def create(self, validated_data):
            user = User(**validated_data)
            user.set_password(validated_data["password"])
            user.save()
            return user

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginApi(APIView):

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        response = Response()
        if (email is None) or (password is None):
            raise exceptions.AuthenticationFailed("email and password required")
        user = User.objects.filter(email=email).first()

        if user is None:
            raise exceptions.AuthenticationFailed("user not found")
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed("wrong password")

        token = get_tokens_for_user(user)
        response.data = token
        return response
    

class UserListApi(APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 25

    class FilterSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=False)
        is_superuser = serializers.BooleanField(required=False, allow_null=True, default=None)
        email = serializers.EmailField(required=False)

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ("id", "email", "first_name", "last_name", "is_superuser")

    def get(self, request):
        # Make sure the filters are valid, if passed
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        users = user_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=users,
            request=request,
            view=self,
        )
