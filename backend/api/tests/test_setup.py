from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from faker import Faker
from django.contrib.auth.models import User
from ..models import Category
from rest_framework_simplejwt.tokens import RefreshToken

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
    

class CategoryTestSetUp(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.category_url = '/api/category/'

        # Admin User
        self.admin_user = User.objects.create_superuser(
            username='admin', email='admin@gmail.com', password='adminpassword'
        )

        # Generate admin JWT token
        refresh = RefreshToken.for_user(self.admin_user)
        self.access_token = str(refresh.access_token)
        
        # Regular User
        self.regular_user = User.objects.create_user(username= 'user', email='user@gmail.com', password='userpassword')

        self.category1 = Category.objects.create(
            name='Year 1 Semmester 1', description="Modules for first semester"
        )
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()