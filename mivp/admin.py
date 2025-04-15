from django.contrib import admin
from .models import Projects, Tasks, Stage
# Register your models here.
admin.site.register(Projects)
admin.site.register(Tasks)
admin.site.site_header = "MIVP Admin"
admin.site.site_title = "MIVP Admin Portal"
admin.site.index_title = "Welcome to MIVP Admin Portal"
admin.site.register(Stage)
# admin.site.register(Tasks)
