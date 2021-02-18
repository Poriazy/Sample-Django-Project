from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog/$', views.posts, name='posts'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/create', views.post_create, name='post_create'),
]