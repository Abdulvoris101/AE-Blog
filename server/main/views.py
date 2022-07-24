from urllib import request
from django.http import Http404
from rest_framework.views import APIView
from .models import Post, Language, Like, Theme
from .serializers import PostSerializer, LanguageSerializer, ThemeSerializer, UserSerializer, LikeSerializer
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions, authentication
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db.models import Count, Q
from rest_framework.authtoken.models import Token


class PostListView(ListCreateAPIView):
    serializer_class = PostSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = Post.objects.all()
        language = self.request.query_params.get('language')
        order_by = self.request.query_params.get('order_by')
        last_posts = self.request.query_params.get('last')
        theme = self.request.query_params.get('theme')

        if theme:
            theme = str(theme).split(',')

            if language:
                language = str(language).split(',')
                queryset = queryset.filter(Q(theme__slug__in=theme) | Q(language__slug__in=language))
            else:
                queryset = queryset.filter(theme__slug__in=theme)

        elif language and order_by:
            language = str(language).split(',')
            queryset = queryset.filter(language__slug__in=language)

            if order_by == 'popular':
                pop_posts = queryset.annotate(num_likes=Count('postlikes', filter=Q(postlikes__status='Like')))
                queryset = pop_posts.order_by('-num_likes')
            else:
                pop_posts = queryset.annotate(num_likes=Count('postlikes', filter=Q(postlikes__status='Like')))
                queryset = pop_posts.order_by(order_by)

        elif last_posts and language:
            language = str(language).split(',')
            queryset = queryset.filter(language__slug__in=language)[:int(last_posts)]
            

        elif language:
            language = str(language).split(',')
            queryset = queryset.filter(language__slug__in=language) 

        elif order_by:
            if order_by == 'popular':
                pop_posts = queryset.annotate(num_likes=Count('postlikes', filter=Q(postlikes__status='Like')))
                queryset = pop_posts.order_by('-num_likes')
            else:
                queryset = Post.objects.order_by(order_by)   


        elif last_posts:
            queryset = Post.objects.all()[:int(last_posts)]
        
        return queryset
    

class PostDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = PostSerializer
    lookup_field = 'slug'
    queryset = Post.objects.all()

class LanguageListView(ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser]
    authentication = [authentication.TokenAuthentication, authentication.BaseAuthentication]
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    lookup_field = 'slug'

class LikePostView(APIView):
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        token = str(request.headers.get('Authorization'))
        token = token.replace('Token', '').strip()

        user = get_object_or_404(Token, key=token).user
        
        is_like = Like.objects.filter(user=user, post=post).exists()
        
        if user:
            if is_like:
                like = Like.objects.get(user=user, post=post)

                if like.status == 'Like':
                    like.status = 'UnLike'
                    
                else:
                    like.status = 'Like'
                
                like.save()
            else:
                like = Like.objects.create(user=user, status='Like', post=post)

        return Response({'liked': True, 'status': like.status})

    
class ThemeListView(APIView):
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        themes = Theme.objects.all()
        serializer = ThemeSerializer(themes, many=True)

        return Response(serializer.data)





    
