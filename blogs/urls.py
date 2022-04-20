from django.urls import path
from blogs import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('article/<int:pk>',views.article,name='article'),
    path('logout',views.signout,name='logout'),
    path('register',views.register,name='register')
]