from django.shortcuts import render
from rest_framework.views import APIView
from main.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.status import *
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist

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
        print(user)
        if user is None:
            raise AuthenticationFailed('Foydalanuvchi topilmadi!')

        if not user.check_password(password):
            raise AuthenticationFailed('Parol Noto\'gri!')
        
        value = request.COOKIES.get('token')
        token = Token.objects.get(user=user)
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

        
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('Unauthenticated') 
        try:
            user = Token.objects.get(key=token).user
        except ObjectDoesNotExist:
            raise AuthenticationFailed('Unauthenticated')

        serializer = UserSerializer(user)

        print(user)

        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('token')
        response.data = {
            'message': 'success',
            'deleted': True
        }