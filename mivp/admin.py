from django.contrib import admin
from .models import Projects, Tasks, Stage, Profile
# Register your models here.






admin.site.site_header = "MIVP Admin"
admin.site.site_title = "MIVP Admin Portal"
admin.site.index_title = "Welcome to MIVP Admin Portal"

# admin.site.register(Tasks)


# Personalización del modelo Project
@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_contacto', 'mail', 'number_contacto', 'direction_contac')
    search_fields = ('name', 'name_contacto', 'mail')
    list_filter = ('name',)

# Personalización del modelo Task
@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'assigned_to', 'stage', 'priority', 'due_date', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('priority', 'stage', 'project')
    date_hierarchy = 'due_date'
    autocomplete_fields = ['project', 'assigned_to', 'stage']

# Personalización del modelo Stage
@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ('name', 'default_user')
    search_fields = ('name',)
    autocomplete_fields = ['default_user']

admin.site.register(Profile)