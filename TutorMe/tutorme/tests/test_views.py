from django.test import TestCase, Client
from django.urls import reverse
from tutorme.models import Category, User, CommonInfo, Student, Teacher, Review
import json


class TestViews(TestCase):
    def test_index_view_GET(self):
        self.client = Client()
        self.index = reverse('index')

        response = self.client.get("index")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tutorme/index.html')