from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import home, projects

class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_projects_url_resolves(self):
        url = reverse('projects')
        self.assertEqual(resolve(url).func, projects)
