from rest_framework import status, exceptions
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView,
    RetrieveUpdateAPIView, RetrieveDestroyAPIView, GenericAPIView
)
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


from common.pagination import (
    PageNumberPagination,
    get_paginated_response
)

from .serializers import (
    ChangePasswordSerializer, 
    UserPasswordResetSerializer,
    UserPasswordSerializer,
    UserRegisterSerializer, 
    UserSerializer)

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


class UserMeApi(RetrieveAPIView): 
        serializer_class = UserSerializer
        model = User
        permission_classes = [IsAuthenticated]

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj
        

class UserChangePasswordApi(RetrieveUpdateAPIView):
        serializer_class = ChangePasswordSerializer
        model = User
        permission_classes = [IsAuthenticated]

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def patch(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserChangeProfileApi(RetrieveUpdateAPIView):
        model = User
        permission_classes = [IsAuthenticated]

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def patch(self, request, *args, **kwargs):
            self.object = self.get_object()
            self.object.profile_image = request.FILES["profile_image"]
            self.object.save()
            response = {"message":'User profile image Updated'}
            return Response(response)


class UserPasswordResetApi(GenericAPIView):
    serializer_class = UserPasswordResetSerializer

    def post(self, request, *args, **kwargs):
        email = request.data['email']

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id) )
            token = PasswordResetTokenGenerator().make_token(user)

            email_send(user=user, uidb64=uidb64, token=token)
        return Response(
            {'successfully':'Check your email to reset your password'},
            status=status.HTTP_200_OK
            )


class UserPasswordTokenCheckApi(GenericAPIView):

    def get(self, request, uidb64, token):
        try:
            id= smart_str(urlsafe_base64_decode(uidb64))
            user= User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response(
                    {'success': False, 
                     'message': 'token is not valid, please request a new one'}, 
                     status=status.HTTP_401_UNAUTHORIZED
                     )
            return Response(
                {'success':True, 
                 'message':'Credential Valid', 
                 'uidb64':uidb64, 
                 'token':token}, 
                 status=status.HTTP_200_OK
                 )


        except DjangoUnicodeDecodeError:
            return Response(
                {'success': False, 
                 'message':'token is not valid, please check the new one'}, 
                 status=status.HTTP_401_UNAUTHORIZED
                 )


class UserSetNewPasswordApi(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserPasswordSerializer

    def post(self, request, *args, **kwargs):
        password = request.data.get("password")
        uidb64 = request.data.get("uidb64")

        id = smart_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=id)

        user.set_password(password)
        user.save()

        return Response(
            {'success':True, 'message':'Password reset successfully'}, 
            status=status.HTTP_200_OK
            )
