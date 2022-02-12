from rest_framework.serializers import ModelSerializer
from .models import Category, Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title', 'image', 'get_absolute_url', 'category', 'content', 'created_at', 'update_at', 'author']

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields  = ['id', 'name', 'get_absolute_url']