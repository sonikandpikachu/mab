from django.contrib import auth

from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, CreateUserSerializer, SignInSerializer


class UserRetreive(RetrieveAPIView):
    """ Returns users info """
    model = User
    serializer_class = UserSerializer


class SignInView(APIView):
    """ POST: sign in with users email and password,
        email -- users email
        password -- users password
        GET: returns current user if he is logged in.
    """
    permission_classes = []
    authentication_classes = []
    serializer_class = SignInSerializer

    def post(self, request, format=None):
        serializer = SignInSerializer(data=request.DATA)
        if serializer.is_valid():
            auth.login(request, serializer.object)
            return Response(status=200)
        else:
            return Response(serializer.errors, status=400)


class UserView(APIView):
    """ GET: returns current user if he is logged in. """

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            serializer = UserSerializer(request.user)
            return Response(serializer.data, status=200)
        else:
            return Response(status=403)


class UserCreate(CreateAPIView):
    """ POST: creates new users by email and password,
    """
    model = User
    serializer_class = CreateUserSerializer
    permission_classes = []
    authentication_classes = []
