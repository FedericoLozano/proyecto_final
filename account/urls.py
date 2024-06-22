from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
]