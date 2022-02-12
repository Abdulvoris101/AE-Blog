from rest_framework.serializers import ModelSerializer, ReadOnlyField, PrimaryKeyRelatedField
from .models import Category, Post
from django.contrib.auth.models import User


class PostSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ['id', 'title',  'content', 'created_at', 'slug', 'get_absolute_url', 'author', 'update_at', 'get_image', 'category']

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields  = ['id', 'name', 'get_absolute_url']
    
class UserSerializer(ModelSerializer):
    posts = PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']
