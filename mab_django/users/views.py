from django.contrib import auth

from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, CreateUserSerializer, SignInSerializer


class SignInView(CreateAPIView):
    """ POST: sign in with users email and password, returns user data with auth_token
        email -- users email
        password -- users password
    """
    permission_classes = []
    authentication_classes = []

    def post(self, request, format=None):
        serializer = SignInSerializer(data=request.DATA)
        if serializer.is_valid():
            user = serializer.object
            auth.login(request, user)
            return Response(SignInSerializer(user).data, status=200)
        else:
            return Response(serializer.errors, status=400)


class UserView(APIView):
    """ GET: returns current user data if he is logged in. """

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            serializer = UserSerializer(request.user)
            return Response(serializer.data, status=200)
        else:
            return Response(status=403)


class UserCreate(CreateAPIView):
    """ POST: creates new users by email and password,
    """
    serializer_class = CreateUserSerializer
    permission_classes = []
    authentication_classes = []


class UserRetreive(RetrieveAPIView):
    """ Returns users info """
    queryset = User.objects.all()
    serializer_class = UserSerializer
