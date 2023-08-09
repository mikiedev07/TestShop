from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .api.serializers import UserRegisterSerializer
from .models import User


class UserRegistration(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {'message': 'User registered successfully.'}
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAuthorization(APIView):
    def post(self, request):
        try:
            username = request.data['username']
            password = request.data['password']
            user = User.objects.get(username=username, password=password)

            if user:
                try:
                    token = RefreshToken.for_user(user)
                    response_data = {
                        'refresh': str(token),
                        'access': str(token.access_token)
                    }
                    return Response(response_data, status=status.HTTP_201_CREATED)
                except Exception:
                    response_data = {'error': 'An error was occurred while creating JWT token'}
                    return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except User.DoesNotExist:
            response_data = {'error': 'Please provide correct email and password'}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

