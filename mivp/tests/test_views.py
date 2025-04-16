from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class ViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='1234')

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_login_required_redirect(self):
        response = self.client.get(reverse('kanban'))
        self.assertRedirects(response, '/login/?next=/kanban')

    def test_authenticated_user_kanban(self):
        self.client.login(username='testuser', password='1234')
        response = self.client.get(reverse('kanban'))
        self.assertEqual(response.status_code, 200)
