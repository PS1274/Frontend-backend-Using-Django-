from django.urls import path
from . import views

urlpatterns=[
  path('index',views.index,name='index'),
  path('counter',views.counter,name='counter'),
  path('register',views.register,name='register'),
  path('login',views.login,name='login'),
  path('logout',views.logout,name='logout'),
  path('blog',views.blog,name='blog'),
  path('post/<str:pk>',views.post,name='post'),
  path('<str:room>/', views.room, name='room'),
  path('', views.home, name='home'),
  path('checkview', views.checkview, name='checkview'),
  path('send', views.send, name='send'),
  path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
  path('contact',views.contact,name='contact'),
  path('send2', views.send2, name='send2'),
]