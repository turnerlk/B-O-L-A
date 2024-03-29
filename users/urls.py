from django.urls import path
from .api import RegisterView, LoginView, LogoutView,VerifyView, ProfileView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('verify', VerifyView.as_view(), name='verify'),
    path('profile/<int:id>/', ProfileView.as_view(), name='profile'),
    path('profile/<str:id>/', ProfileView.as_view(), name='profile_str'),
    
    
]
