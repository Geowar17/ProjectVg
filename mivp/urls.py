from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('projects/', views.projects, name='projects'),
    path('tasks/', views.tasks, name='tasks'),
    path('create_project/', views.create_project, name='create_project'),
    path('create_tasks/', views.create_tasks, name='create_tasks'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create_stage/', views.create_stage, name='create_stage'),
    path('stages/', views.stage_list, name='stage_list'),
    path('task/<int:task_id>/advance/', views.advance_stage, name='advance_stage'),
    path('task/<int:task_id>/back/', views.back_stage, name='back_stage'),
    path('kanban/', views.kanban_board, name='kanban'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('documents/<int:doc_id>/delete/', views.delete_document, name='delete_document'),
    path('project/', views.archived_projects, name='archived_projects'),
    path('task/', views.completed_tasks, name='completed_tasks'),
    path('search/', views.search_archived_and_completed, name='archived_search'),
    path('project/<int:project_id>/unarchive/', views.unarchive_project, name='unarchive_project'),
    path('project/<int:project_id>/archive/', views.archive_project, name='archive_project'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)