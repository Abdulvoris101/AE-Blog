from django.http import Http404
from rest_framework.views import APIView
from .models import Post, Category, Like
from .serializers import PostSerializer, CategorySerializer, UserSerializer, LikeSerializer
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions, authentication
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class PostListView(ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = Post.objects.all()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__slug=category)
        
        return queryset
    

class PostDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]
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

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication, authentication.BaseAuthentication]

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        
        
        try:
            get_like = Like.objects.get(user=request.user, post=post)

            if get_like.status == 'Like':
                get_like.status = 'UnLike'

                get_like.save()

                return Response({
                    'status': 'UnLike',
                    'post_id': post.title
                })

            get_like.status = 'Like'

            get_like.save()

            return Response({
                'status': 'Like',
                'post_id': post.title
            })

            

        except Like.DoesNotExist:
            like = Like.objects.create(user=request.user, post=post, status='Like')

            return Response({
                'status': 'Like',
                'post_id': post.title
            })
            
    
    
