from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='bloghome'),
    path('search/', views.search, name='search'),
    path('blogpost/<str:slug>', views.blogpost, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.handleSignUp, name="handleSignUp"),
    path('login/', views.handleLogin, name="handleLogin"),
    path('logout/', views.handleLogout, name="handleLogout"),
    path('blogpost/postComment/', views.postComment, name="postComment"),
]
