from django.test import TestCase
from django.urls import reverse
from .models import Client, HealthProgram

class ClientCreateViewTestCase(TestCase):
    def setUp(self):
        self.program = HealthProgram.objects.create(name="Test Program")

    def test_create_client_with_valid_data(self):
        response = self.client.post(reverse('client_create'), {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone': '1234567890',
            'date_of_birth': '1990-01-01',
            'programs': [self.program.id],
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful creation
        self.assertTrue(Client.objects.filter(email='john.doe@example.com').exists())

    def test_create_client_with_invalid_data(self):
        response = self.client.post(reverse('client_create'), {
            'first_name': '',
            'last_name': 'Doe',
            'email': 'invalid-email',
            'phone': '',
            'date_of_birth': '',
        })
        self.assertEqual(response.status_code, 200)  # Should stay on the form page with errors
        self.assertFormError(response, 'form', 'first_name', 'This field is required.')
