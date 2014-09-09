from django.contrib import auth

from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from mailing import send_templated_email
from .models import User
from .serializers import UserSerializer, CreateUserSerializer, SignInSerializer


class SignInView(APIView):
    """ Sign in with users email and password, returns user data with auth_token
    """
    serializer_class = SignInSerializer
    permission_classes = []
    authentication_classes = []

    def post(self, request, format=None):
        serializer = SignInSerializer(data=request.DATA)
        if serializer.is_valid():
            user = serializer.object
            auth.login(request, user)
            return Response(UserSerializer(user).data, status=200)
        else:
            return Response(serializer.errors, status=400)


class UserView(APIView):
    """ Returns current user data if he is logged in. """

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=200)


class UserCreate(CreateAPIView):
    """ Creates new user and returns his auth token
    """
    serializer_class = CreateUserSerializer
    permission_classes = []
    authentication_classes = []

    def post_save(self, obj, created=False):
        if created:
            send_templated_email('signup', {}, recipients=[obj])


class UserRetreive(RetrieveAPIView):
    """ Returns users info """
    queryset = User.objects.all()
    serializer_class = UserSerializer
