from django.conf import settings
from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


def index(request):
    return render(request, 'index.html', {})


class LoginViewUserCredentials(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username_field = getattr(settings, 'USERNAME_FIELD_JWT', 'username')
        password_field = getattr(settings, 'PASSWORD_FIELD_JWT', 'password')
        username = request.data.get(username_field)
        password = request.data.get(password_field)

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        return Response({
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh)
        })
