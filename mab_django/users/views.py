from django.contrib import auth

from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, CreateUserSerializer, SignInSerializer


class UserCreate(CreateAPIView):
    model = User
    serializer = CreateUserSerializer
    permission_classes = []
    authentication_classes = []


class UserRetreive(RetrieveAPIView):
    model = User
    serializer = UserSerializer

    def post_save(self, user):
        auth.login(self.request, user)


class SignInView(APIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request, format=None):
        serializer = SignInSerializer(data=request.DATA)
        if serializer.is_valid():
            auth.login(request, serializer.object)
            return Response(status=200)
        else:
            return Response(serializer.errors, status=400)
