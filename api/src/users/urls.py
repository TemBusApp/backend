from django.urls import path
from users.views import register, hello, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('hello/', hello, name='hello'),
]
