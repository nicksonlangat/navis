from rest_framework import status, exceptions
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.generics import (
    CreateAPIView, ListAPIView, 
    RetrieveUpdateAPIView, RetrieveDestroyAPIView
)

from common.pagination import (
    PageNumberPagination,
    get_paginated_response
)

from .serializers import UserRegisterSerializer, UserSerializer
from .models import User
from .selectors import user_list
from .services import get_tokens_for_user, user_update



class UserRegisterApi(CreateAPIView):

    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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
    

class UserListApi(ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView):
    class Pagination(PageNumberPagination):
        page_size = 13
    
    serializer_class = UserSerializer
    queryset = user_list()

    def get(self, request, *args, **kwargs):
        users = user_list(filters=request.query_params)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.serializer_class,
            queryset=users,
            request=request,
            view=self,
        )
    
    def patch(self, request, pk, format=None):  
        user = User.objects.get(id=pk)
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            user_update(user, data=serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        user = User.objects.get(id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
