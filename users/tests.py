from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SignupPageView

# Create your tests here.

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user (
            username = 'dede',
            email = 'dede@gmail.com',
            password='password123'
        )

        self.assertEqual(user.username, 'dede')
        self.assertEqual(user.email, 'dede@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username = 'david',
            email = 'david@gmail.com',
            password = 'password123'
        )

        self.assertEqual(admin_user.username, 'david')
        self.assertEqual(admin_user.email, 'david@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTests(TestCase):

    def test_signup_template(self):
        response = self.client.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertContains(response, 'Sign Up')
        self.assertNotContains(response, 'Log In')

    def test_signup_form(self):
        response = self.client.get(reverse('users:signup'))
        form = response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
