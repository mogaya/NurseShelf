from .test_setup import CategoryTestSetUp
from rest_framework import status
from ..models import Category
from rest_framework_simplejwt.tokens import RefreshToken

class CategoryTests(CategoryTestSetUp):
    def test_list_categories(self):
        res = self.client.get(self.category_url)

        # import pdb
        # pdb.set_trace()

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], self.category1.name)

    def test_create_category(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        
        data = {
            'name': 'Year1 Semmester2',
            'description': 'Modules for 1st Yr, 2nd Sem'
        }
        res = self.client.post(self.category_url, data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['name'], 'Year1 Semmester2')
        self.assertEqual(Category.objects.count(), 2)

    def test_retrieve_category(self):
        res = self.client.get(f'{self.category_url}{self.category1.id}/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['name'], self.category1.name)

    def test_update_category(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        data = {'name': 'Updated Category Name', 'description': 'Updated Description'}
        res = self.client.put(f'{self.category_url}{self.category1.id}/', data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_category(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        res = self.client.delete(f'{self.category_url}{self.category1.id}/')
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)

    def test_permission_for_regular_user(self):
        self.client.logout()
        
        regular_refresh = RefreshToken.for_user(self.regular_user)
        self.regular_access_token = str(regular_refresh.access_token)

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.regular_access_token}')

        # Attempt creating a category
        data = {"name": "Unauthorized Category", "description": "Should Fail"}
        res = self.client.post(self.category_url, data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

        # Attempt to update a category
        data = {'name': 'Unauthorized Update'}
        res = self.client.put(self.category_url, data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

        # Attempt to delete
        self.client.delete(f'{self.category_url}{self.category1.id}/')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)