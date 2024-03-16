from django.contrib import admin
from django.urls import path, include
from users.views import login_view, register_view, dashboard_view, profile_view, index_view
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('profile/', profile_view, name='profile'),
    path('', index_view, name='index'),
]