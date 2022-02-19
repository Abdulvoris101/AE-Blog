from unicodedata import name
from django.urls import path
from .views import PostListView, CategoryListView, PostDetailView, CategoryDetailView

urlpatterns = [
    path('posts/', PostListView.as_view()),
    path('categories/', CategoryListView.as_view()),
    path('post/<slug:slug>', PostDetailView.as_view()),
    path('category/<slug:slug>', CategoryDetailView.as_view()),

]
