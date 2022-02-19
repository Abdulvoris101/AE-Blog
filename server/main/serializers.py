from enum import unique
from rest_framework.serializers import ModelSerializer, ReadOnlyField, PrimaryKeyRelatedField
from .models import Category, Post
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from .utils import get_random_code
from rest_framework import serializers

class PostSerializer(ModelSerializer, serializers.Serializer):
    author = ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'title',  'content', 'created_at', 'get_absolute_url', 'slug', 'author', 'update_at', 'get_image', 'category']
        
    def create(self, validated_data):
        if not validated_data['slug']:
            ex = False
            to_slug = slugify(validated_data['title'])
            ex = Post.objects.filter(slug=to_slug).exists()

            while ex:
                to_slug = slugify(to_slug + ' ' + str(get_random_code()))
                ex = Post.objects.filter(slug=to_slug).exists()
            
            validated_data['slug'] = to_slug

        return Post.objects.create(**validated_data)




class CategorySerializer(ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields  = ['id', 'name', 'get_absolute_url', 'slug', 'posts']
    
class UserSerializer(ModelSerializer):
    posts = PrimaryKeyRelatedField(many=True, read_only=True)
    
    
    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'first_name', 'email', 'password',]
        read_only_fields = ('id', 'posts')
        write_only_fields = ('password', )
        extra_kwargs = {'first_name': {'required': True}} 
        extra_kwargs = {'email': {'required': True}} 

    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
