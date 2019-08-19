from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app.model.users import UserProfile
from app.api.users.serializers import UserProfileSerializer


@permission_classes((IsAdminUser, IsAuthenticated))
class UserCreate(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        type = data['type']

        user_check = User.objects.filter(username=username)
        if not user_check:
            new_user = User.objects.create_user(username=username, password=password)
            token, _ = Token.objects.get_or_create(user=new_user)
            new_user.userprofile.type = type
            new_user.userprofile.save()
            new_user.save()
            return Response("User is created")
        else:
            return Response("We have already the same username")


@permission_classes((AllowAny,))
class UserLogin(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password!'})
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid credentials!'})
        token, _ = Token.objects.get_or_create(user=user)
        profile = UserProfile.objects.get(user=user)
        return Response({'token': token.key,
                         'user_id': user.id,
                         'username': user.username,
                         'user_type': profile.get_type_display()})


@permission_classes((IsAuthenticated,))
class UserLogout(APIView):
    def get(self, request, format=None):
        if request.user:
            request.user.auth_token.delete()
        else:
            Response("Please login first")
        return Response("Successfully logged out")


class UserListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
