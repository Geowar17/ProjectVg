from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('projects/', views.projects, name='projects'),
    path('tasks/', views.tasks, name='tasks'),
    path('create_project/', views.create_project, name='create_project'),
    path('create_tasks/', views.create_tasks, name='create_tasks'),
    path('create_tasks/', views.create_tasks, name='create_tasks'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]