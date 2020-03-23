from django.test import TestCase
from django.urls import reverse


class UrlTest(TestCase):
    def test_about_url(self):
        response = self.client.get('/tutorme/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_url_reverse(self):
        response = self.client.get(reverse('tutorme:about'))
        self.assertEqual(response.status_code, 200)

    def test_index_url(self):
        response = self.client.get('/tutorme/')
        self.assertEqual(response.status_code, 200)

    def test_index_url_reverse(self):
        response = self.client.get(reverse('tutorme:index'))
        self.assertEqual(response.status_code, 200)

    def test_login_url(self):
        response = self.client.get('/tutorme/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_url_reverse(self):
        response = self.client.get(reverse('tutorme:login'))
        self.assertEqual(response.status_code, 200)

