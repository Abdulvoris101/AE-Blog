from django.http import Http404
from rest_framework.views import APIView
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions, authentication
from django.contrib.auth.models import User

class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication, authentication.BaseAuthentication]
    serializer_class = PostSerializer
    lookup_field = 'slug'
    queryset = Post.objects.all()

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser]
    authentication = [authentication.TokenAuthentication, authentication.BaseAuthentication]

    serializer_class = CategorySerializer
    lookup_field = 'slug'
    queryset = Category.objects.all()
