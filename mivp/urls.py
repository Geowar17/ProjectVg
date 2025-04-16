from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('projects/', views.projects, name='projects'),
    path('tasks/', views.tasks, name='tasks'),
    path('create_project/', views.create_project, name='create_project'),
    path('create_tasks/', views.create_tasks, name='create_tasks'),
    path('create_tasks/', views.create_tasks, name='create_tasks'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create_stage/', views.create_stage, name='create_stage'),
    path('stages/', views.stage_list, name='stage_list'),
    path('task/<int:task_id>/advance/', views.advance_stage, name='advance_stage'),
    path('task/<int:task_id>/back/', views.back_stage, name='back_stage'),
    path('kanban/', views.kanban_board, name='kanban'),

]