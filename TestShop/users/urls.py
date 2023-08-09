from django.urls import path

from .views import UserRegistration, UserAuthorization

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('login/', UserAuthorization.as_view(), name='login')
]
