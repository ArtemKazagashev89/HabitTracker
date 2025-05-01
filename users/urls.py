from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserCreateApiView, UserDestroyApiView, UserListApiView, UserRetrieveApiView, UserUpdateApiView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("register/", UserCreateApiView.as_view(), name="register"),
    path("users/", UserListApiView.as_view(), name="user-list"),
    path("user/<int:pk>/", UserRetrieveApiView.as_view(), name="user-detail"),
    path("user/update/", UserUpdateApiView.as_view(), name="user-update"),
    path("user/delete/", UserDestroyApiView.as_view(), name="user-delete"),
]
