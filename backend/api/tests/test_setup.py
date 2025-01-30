from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from faker import Faker
from django.contrib.auth.models import User
from ..models import Category, Module
from rest_framework_simplejwt.tokens import RefreshToken

class BaseTestSetup(APITestCase):
    def setUp(self):
        self.client = APIClient()

        # URLs
        self.register_url = '/api/user/'
        self.token_url = reverse('get_token')
        self.refresh_token_url = reverse('refresh')
        self.category_url = '/api/category/'
        self.module_url = '/api/module/'

        # Creating Admin User
        self.admin_user = User.objects.create_superuser(username='admin', email='admin@gmail.com', password='adminpassword')

        # Generating JWT token for admin
        refresh = RefreshToken.for_user(self.admin_user)
        self.access_token = str(refresh.access_token)

        self.fake = Faker()
        email = self.fake.email()
        
        self.user_data = {
            'email': email,
            'username': email.split('@')[0],
            'password': email,
        }

        # Creating a regular User
        self.regular_user = User.objects.create_user(username='user', email='user@gmail.com', password='userpassword')

        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    

class CategoryTestSetUp(BaseTestSetup):
    def setUp(self):

        self.category1 = Category.objects.create(
            name='Year 1 Semmester 1', description="Modules for first semester"
        )

        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
class ModuleTestSetUp(BaseTestSetup):
    def setUp(self):

        self.category = Category.objects.create(
            name='Year 1 Semmester 1', description="Modules for first semester"
        )

        self.module1 = Module.objects.create(
            code='COM 1103', name= "Communication", description= "This Module has Communication Resources",category= self.category
        )

        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()