from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from main.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.status import *
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist
import json
from rest_framework import permissions, authentication

class CreateUserView(APIView):
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                response = Response()
                response.set_cookie(key='token', value=token, httponly=True)
                
                response.data = {
                    'token': token.key,
                    'message': 'success',
                    'created': True
                }
                return response

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    
class LoginUserView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('Foydalanuvchi topilmadi!')

        if not user.check_password(password):
            raise AuthenticationFailed('Parol Noto\'gri!')
        
        value = request.COOKIES.get('token')
        token = get_object_or_404(Token, user=user)
        response = Response()

        if value is None:
            response.set_cookie(key='token', value=token, httponly=True)

        response.data = {
            'token': token.key,
            'message': 'success',
            'logged in': True
        }
        print(request.user)
            
        return response

class UserList(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
        
class UserView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request):
        token = request.headers.get('Authorization')
        token_cookie = request.COOKIES.get('token')
        token_str = str(token)
        token_str = token_str.replace('Token', '').strip()

        if token:
            user = Token.objects.get(key=token_str).user
            serializer = UserSerializer(user)
        elif token_cookie:
            user = Token.objects.get(key=token_cookie).user
            serializer = UserSerializer(user)
        else:
            raise AuthenticationFailed('Unauthenticated')
        
        return Response(serializer.data)

class LogoutView(APIView):
    def get(self, request):
        response = Response()
        response.delete_cookie('token')

        response.data = {
            'message': 'success',
            'deleted': True
        }

        return response