from django.urls import path
from .views import PostListView, LanguageListView, ThemeListView, PostDetailView, LanguageDetailView, LikePostView

urlpatterns = [
    path('posts/', PostListView.as_view()),
    path('languages/', LanguageListView.as_view()),
    path('post/<slug:slug>', PostDetailView.as_view()),
    path('language/<slug:slug>', LanguageDetailView.as_view()),
    path('like/<int:pk>/', LikePostView.as_view()),
    path('themes/', ThemeListView.as_view())

]
