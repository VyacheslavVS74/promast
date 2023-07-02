from django.urls import path
from . import views

urlpatterns = [
    # path('', BlogHome.as_view(), name='blog'),
    # path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    # path('category/<slug:cat_slug>/', BlogCategory.as_view(), name='category'),

    path('', views.blog_home, name='blog'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('category/<slug:cat_slug>/', views.blog_category, name='category'),
]
