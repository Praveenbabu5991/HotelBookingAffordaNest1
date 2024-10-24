from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import login as django_login, logout as django_logout
from .models import CustomUser
from .serializers import UserRegistrationSerializer, UserLoginSerializer, ChangePasswordSerializer
from rest_framework.authtoken.models import Token
class UserViewSet(viewsets.ViewSet):
    # API for user registration
    @action(detail=False, methods=['post'], url_path='register')
    def register(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        print("Received request data:", request.data)  # Debugging line
        
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data # Assuming your serializer returns the user
            django_login(request, user)  # Log in the user session
            
            # Get or create token for the user
            token, created = Token.objects.get_or_create(user=user)
            
            # Return the token in the response
            return Response({
                "message": "Login successful",
                "token": token.key  # Include the token in the response
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # API for changing the password
    @action(detail=False, methods=['post'], url_path='change-password')
    def change_password(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='logout')
    def logout(self, request):
        django_logout(request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
