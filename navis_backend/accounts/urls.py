from django.urls import path

from .views import UserListApi, UserCreateApi, UserLoginApi

urlpatterns = [
    path("users", UserListApi.as_view(), name="list"),
    path("register", UserCreateApi.as_view(), name="create"),
    path("login", UserLoginApi.as_view(), name="login"),
]
