from django.urls import path
from .views import CreateUserView, LoginUserView, UserView, LogoutView

urlpatterns = [
    path('register/', CreateUserView.as_view()),
    path('login/', LoginUserView.as_view()),
    path('info/', UserView.as_view()),
    path('logout/', LogoutView.as_view())
]
