from django.urls import path

from .views import UserListApi, UserRegisterApi, UserLoginApi

urlpatterns = [
    path("users", UserListApi.as_view(), name="users"),
    path("users/<uuid:pk>/", UserListApi.as_view(), name="user"),
    path("register/", UserRegisterApi.as_view(), name="register"),
    path("login/", UserLoginApi.as_view(), name="login"),
]
