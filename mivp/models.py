from django.db import models
from django.contrib.auth.models import User

# Modelo de proyectos
class Projects(models.Model):
    name = models.CharField(max_length=200)
    name_contacto = models.CharField(max_length=200)
    number_contacto = models.CharField(max_length=20)
    mail = models.EmailField()
    direction_contac = models.CharField(max_length=200)
    is_archived = models.BooleanField(default=False)  # 🔥 NUEVO

    def __str__(self):
        return self.name

# Modelo de etapas del flujo de trabajo (Kanban)
class Stage(models.Model):
    ROLE_CHOICES = [
        ('comercial', 'Comercial'),
        ('gerencia', 'Gerencia'),
        ('cliente', 'Cliente'),
        ('operaciones', 'Operaciones'),
    ]

    name = models.CharField(max_length=100)
    default_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Usuario asignado por defecto a esta etapa"
    )
    responsible_role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='comercial',
        help_text="Rol que puede gestionar esta etapa"
    )

    def __str__(self):
        return self.name

# Modelo de tareas
class Tasks(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Baja'),
        ('medium', 'Media'),
        ('high', 'Alta'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name="tasks")
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_tasks")
    stage = models.ForeignKey(Stage, on_delete=models.SET_NULL, null=True, blank=True, related_name="tasks")
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)  # 🔥 NUEVO

    def __str__(self):
        return f"{self.title} - {self.project.name}"

# Perfil de usuario con rol
class Profile(models.Model):
    ROLE_CHOICES = [
        ('comercial', 'Comercial'),
        ('gerencia', 'Gerencia'),
        ('cliente', 'Cliente'),
        ('operaciones', 'Operaciones'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='comercial')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Documentos asociados a proyectos
class ProjectDocument(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='documents')
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='project_docs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

