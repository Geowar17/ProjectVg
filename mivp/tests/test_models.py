from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Projects, Tasks, Stage
from datetime import date

class ModelsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.project = Projects.objects.create(
            name="Test Project",
            name_contacto="Cliente",
            number_contacto="123456789",
            mail="cliente@test.com",
            direction_contac="Calle Falsa 123"
        )
        self.stage = Stage.objects.create(name="Inicio", default_user=self.user)

    def test_project_str(self):
        self.assertEqual(str(self.project), "Test Project")

    def test_stage_str(self):
        self.assertEqual(str(self.stage), "Inicio")

    def test_task_creation(self):
        task = Tasks.objects.create(
            title="Test Task",
            description="Una tarea de prueba",
            project=self.project,
            assigned_to=self.user,
            stage=self.stage,
            priority="high",
            due_date=date.today()
        )
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.priority, "high")
