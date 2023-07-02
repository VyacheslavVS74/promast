from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_users, name='login'),
    path('logout/', views.logout_users, name='logout'),
    path('register/', views.register_users, name='register'),
]

