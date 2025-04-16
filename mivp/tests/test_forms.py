from django.test import TestCase
from ..forms import ProjectNewForm

class ProjectFormTest(TestCase):
    def test_valid_project_form(self):
        form_data = {
            'name': 'Proyecto Prueba',
            'name_contacto': 'Juan',
            'number_contacto': '987654321',
            'mail': 'juan@example.com',
            'direction_contac': 'Av. Siempre Viva 123'
        }
        form = ProjectNewForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_project_form(self):
        form = ProjectNewForm(data={})
        self.assertFalse(form.is_valid())
