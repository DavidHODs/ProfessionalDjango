from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pages.views import HomePageView


# Create your tests here.

class HomePageTests(SimpleTestCase):

    def setup(self):
        url = reverse('pages:home')
        self.response = self.client.get(url) 

    def test_homepage_statuscode(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_urlname(self):
        response = self.client.get(reverse('pages:home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get(reverse('pages:home'))
        view = resolve('/')
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'HomePage')
        self.assertNotContains(response, 'Linux sys')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)