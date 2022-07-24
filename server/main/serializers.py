from rest_framework.serializers import ModelSerializer, ReadOnlyField, PrimaryKeyRelatedField, SlugRelatedField, StringRelatedField
from .models import Language, Post, Like, Theme
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from .utils import get_random_code
from rest_framework import serializers


class LikeSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.username')

    class Meta:
        model = Like
        fields  = ['id', 'user', 'post', 'status']

class PostSerializer(ModelSerializer, serializers.Serializer):
    author = ReadOnlyField(source='author.username')
    theme = StringRelatedField()
    language = StringRelatedField()
    likes = LikeSerializer(source='postlikes', many=True)


    class Meta:
        model = Post    
        fields = ['id', 'title', 'content', 'likes', 'num_likes', 'theme', 'created_at', 'get_thumbnail', 'get_absolute_url', 'slug', 'author', 'update_at', 'image', 'language']
        
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

    def to_representation(self, instance):
        representation = super(PostSerializer, self).to_representation(instance)
        representation['created_at'] = instance.created_at.strftime('%d %a %H:%M')
        return representation


class LanguageSerializer(ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    
    class Meta:
        model = Language
        fields  = ['id', 'name', 'get_absolute_url', 'slug', 'posts']


class ThemeSerializer(ModelSerializer):
    theme = SlugRelatedField(many=True, read_only=True, slug_field='slug')

    class Meta:
        model = Theme
        fields = ['id', 'name', 'slug', 'theme']

class UserSerializer(ModelSerializer):
    posts = PrimaryKeyRelatedField(many=True, read_only=True)
    userlikes = PrimaryKeyRelatedField(many=True, read_only=True)
    
    
    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'first_name', 'email', 'password', 'userlikes']
        read_only_fields = ('id', 'posts')
        write_only_fields = ('password', )
        extra_kwargs = {'email': {'required': True}} 

    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

