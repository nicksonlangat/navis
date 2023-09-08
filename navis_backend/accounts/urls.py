from django.urls import path

from .views import UserListApi, UserRegisterApi, UserLoginApi, UserMeApi, UserChangePasswordApi, UserChangeProfileApi

urlpatterns = [
    path("users", UserListApi.as_view(), name="users"),
    path("users/me", UserMeApi.as_view(), name="users-me"),
    path("users/password/change", UserChangePasswordApi.as_view(), name="users-password-change"),
    path("users/profile", UserChangeProfileApi.as_view(), name="users-profile-change"),
    path("users/<uuid:pk>/", UserListApi.as_view(), name="user"),
    path("register/", UserRegisterApi.as_view(), name="register"),
    path("login/", UserLoginApi.as_view(), name="login"),
]
