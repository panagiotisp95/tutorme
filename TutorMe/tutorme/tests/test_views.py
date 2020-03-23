from tutorme.models import User,Teacher
from django.urls import reverse
from django.test.client import Client
from django.test import TestCase


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('panayiotis@tutorme.com', 'password')
        Teacher.objects.create(user=self.user, first_name='Panayiotis')

    def test_about(self):
        self.client.login(email='panayiotis@tutorme.com', password='password')
        response = self.client.get(reverse('tutorme:about'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard(self):
        self.client.login(email='panayiotis@tutorme.com', password='password')
        response = self.client.get(reverse('tutorme:dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        self.client.login(email='panayiotis@tutorme.com', password='password')
        response = self.client.get(reverse('tutorme:index'))
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        self.client.login(email='panayiotis@tutorme.com', password='password')
        response = self.client.get(reverse('tutorme:search'))
        self.assertEqual(response.status_code, 200)


