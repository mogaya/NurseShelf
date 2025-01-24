from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from . test_setup import TestSetup

class AuthenticationTests(TestSetup):

    def test_not_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_correctly(self):
        res = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(res.data['email'], self.user_data['email'])
        self.assertEqual(res.data['username'], self.user_data['username'])
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_obtain_token(self):
        self.client.post(self.register_url, self.user_data, format="json")  
        data = {'username': self.user_data['username'], 'password': self.user_data['password']}
        res = self.client.post(self.token_url, data, format='json')

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('access', res.data)
        self.assertIn('refresh', res.data)