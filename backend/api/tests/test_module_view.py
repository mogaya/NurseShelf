from .test_setup import ModuleTestSetUp
from rest_framework import status
from ..models import Module

class ModuleTests(ModuleTestSetUp):
    def test_everyone_can_list(self):
        res = self.client.get(self.module_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        self.assertEqual(len(res.data), 2)
        self.assertEqual(res.data[0]['name'], self.module1.name)

    def test_everyone_can_retrieve(self):
        res = self.client.get(f'{self.module_url}{self.module1.id}/')

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['name'], self.module1.name)

    def test_admin_can_create_update_delete(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # Admin can add a module

        data = {
            'code': 'CAN 1102',
            'name': 'Applied Communication in Nursing',
            'description': 'Applied Communication in Nursing Content',
            'category': self.category.id
        }

        res = self.client.post(self.module_url, data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Module.objects.count(), 3)

        # Admin can update a module

        data = {
            'code': 'Editted Code',
            'name': 'Updated Name',
            'description': 'Updated Desc',
            'category': self.category.id
        }

        res = self.client.put(f'{self.module_url}{self.module1.id}/', data, format='json')
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # Refreshing from db to verify updates
        self.module1.refresh_from_db()
        self.assertEqual(self.module1.code, 'Editted Code')
        self.assertEqual(self.module1.name, 'Updated Name')

        # Admin can Delete a module
        res = self.client.delete(f'{self.module_url}{self.module1.id}/')

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Module.objects.count(), 2)

    def test_user_cannot_create_update_delete(self):
        self.client.logout()
        
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.regular_access_token}')

        # Reg User cannot add module
        data = {
            'code': 'CAN 1102',
            'name': 'Applied Communication in Nursing',
            'description': 'Applied Communication in Nursing Content',
            'category': self.category.id
        }

        res = self.client.post(self.module_url, data)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

        # Reg User cannot update module
        data = {
            'code': 'Editted Code',
            'name': 'Updated Name',
            'description': 'Updated Desc',
            'category': self.category.id
        }
        res = self.client.put(f'{self.module_url}{self.module1.id}/', data, format='json')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

        # Reg User cannot delete module
        res = self.client.delete(f'{self.module_url}{self.module2.id}/')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)