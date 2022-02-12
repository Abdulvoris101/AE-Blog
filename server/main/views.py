from django.http import Http404
from rest_framework.views import APIView
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.generics import ListCreateAPIView
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions

class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get_object(self, slug):
        try:
            return Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            raise Http404
    
    def get(self, request, slug, format=None):
        post = self.get_object(slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, slug, format=None):
        post = self.get_object(slug)
        serializer = PostSerializer(post, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class CategoryListView(APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save()

class CategoryDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser]
    def get_object(self, request, slug):
        try:
            Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, slug, format=None):
        category = self.get_object(slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, slug, format=None):
        category = self.get_object(slug)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, slug, format=None):
        category = self.get_object(slug)
        category.delete()
        return Response(status=HTTP_204_NO_CONTENT)