from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

from descriptions.tests import TestDescriptions

User = get_user_model()


class RegisterUserTests(TestCase):

    invalid_user = {
        'username': 'denis' + 'd' * 150,
        'email': 'denisemailcom',
        'password': '1234567890'
    }

    simple_valid_user = {
        'username': 'denise',
        'email': 'denise@email.com',
        'password': 'MYPASSWORD_myp455w0rd',
    }

    full_valid_user = {
        'username': 'denis',
        'email': 'denis@email.com',
        'password': 'MYPASSWORD_myp455w0rd',
        'first_name': 'Denis',
        'last_name': 'Lastname',
        'phone': '55 11 99999 9999'
    }

    check_fields = ['username', 'email', 'first_name', 'last_name', 'phone']
    profile = reverse('profile')
    route = '/api/register/'
    login = '/api/login/'

    def setUp(self):
        self.client = APIClient()

    def create_valid_user(self):
        user_test = User.objects.create_user(**self.simple_valid_user)
        return user_test

    def test_not_allowed_methods(self):
        response = self.client.get(self.route)
        with self.subTest('GET must return method not allowed', response=response):
            self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
            self.assertIn('detail', response.json())
            self.assertIn('not allowed', response.json().get('detail').lower())

        response = self.client.put(self.route, data={}, format='json')
        with self.subTest('PUT must return method not allowed', response=response):
            self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
            self.assertIn('detail', response.json())
            self.assertIn('not allowed', response.json().get('detail').lower())

        response = self.client.patch(self.route, data={}, format='json')
        with self.subTest('PATCH must return method not allowed', response=response):
            self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
            self.assertIn('detail', response.json())
            self.assertIn('not allowed', response.json().get('detail').lower())

        response = self.client.delete(self.route)
        with self.subTest('DELETE must return method not allowed', response=response):
            self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
            self.assertIn('detail', response.json())
            self.assertIn('not allowed', response.json().get('detail').lower())

    def test_invalid_register(self):
        response = self.client.post(self.route, data={}, format='json')
        with self.subTest('Username, email and password must be required', response=response):
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            body = response.json()
            self.assertIn('email', body)
            self.assertIn('password', body)
            self.assertIn('username', body)

        response = self.client.post(self.route, data=self.invalid_user, format='json')
        with self.subTest('User fields must be valid', response=response):
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            body = response.json()
            self.assertIn('email', body)
            self.assertIn('password', body)
            self.assertIn('username', body)

    def test_valid_register(self):
        data = self.simple_valid_user
        response = self.client.post(self.route, data=data, format='json')
        with self.subTest('User must be registered with only required fields', response=response):
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            user = response.json()

            self.assertEqual(data.get('email'), user.get('email'))
            self.assertEqual(data.get('username'), user.get('username'))

            db_users = User.objects.count()
            self.assertEqual(1, db_users)

        data = self.full_valid_user
        response = self.client.post(self.route, data=data, format='json')
        with self.subTest('User must be registered with all fields', response=response):
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            user = response.json()

            for field in self.check_fields:
                self.assertEqual(data.get(field), user.get(field))

            db_users = User.objects.count()
            self.assertEqual(2, db_users)

    def test_invalid_login(self):
        data = self.simple_valid_user
        response = self.client.post(self.login, data=data, format='json')
        with self.subTest('Username and/or password must be valid', response=response):
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_login(self):
        data = self.simple_valid_user
        self.client.post(self.route, data=data, format='json')
        response = self.client.post(self.login, data=data, format='json')
        with self.subTest('Username and/or password must be valid', response=response):
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIn('token', response.json())

    def test_profile_retrieve(self):
        user_test = self.create_valid_user()
        self.client.force_authenticate(user_test)
        response = self.client.get(self.profile, format='json')
        with self.subTest('Authentication credentials must be provided', response=response):
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIn('name', response.json())
            self.assertIn('descriptions', response.json())