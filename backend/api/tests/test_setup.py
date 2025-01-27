from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker

class TestSetup(APITestCase):
    def setUp(self):
        self.register_url = '/api/user/'
        self.token_url = reverse('get_token')
        self.refresh_token_url = reverse('refresh')

        self.fake = Faker()
        email = self.fake.email()
        
        self.user_data = {
            'email': email,
            'username': email.split('@')[0],
            'password': email,
        }

        # import pdb
        # pdb.set_trace()

        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    