from django.urls import path

from .views import (
    UserRegisterApi,
    UserLoginApi,
    UserPasswordResetApi,
    UserPasswordTokenCheckApi,
    UserSetNewPasswordApi,
    UserListApi,
    UserMeApi,
    UserChangePasswordApi,
    UserChangeProfileApi
    )

urlpatterns = [
    path("register/", UserRegisterApi.as_view(), name="register"),
    path("login/", UserLoginApi.as_view(), name="login"),
    path("password/reset/", UserPasswordResetApi.as_view(), name="password-reset"),
    path('password-reset/<uidb64>/<token>/', UserPasswordTokenCheckApi.as_view(),name='token-check'),
    path('new/password/', UserSetNewPasswordApi.as_view(),name='new-password'),
    path("users", UserListApi.as_view(), name="users"),
    path("users/me", UserMeApi.as_view(), name="users-me"),
    path("users/password/change", UserChangePasswordApi.as_view(), name="users-password-change"),
    path("users/profile", UserChangeProfileApi.as_view(), name="users-profile-change"),
    path("users/<uuid:pk>/", UserListApi.as_view(), name="user"),
]
