from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import UserCreateSerializers, UserSerializer


class UserCreateApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializers


class UserListApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserRetrieveApiView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserUpdateApiView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserDestroyApiView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
