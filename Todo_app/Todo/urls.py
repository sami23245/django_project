from django.contrib import admin
from django.urls import path
from Todo import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('todo/', views.todo_view, name='todo'),
]