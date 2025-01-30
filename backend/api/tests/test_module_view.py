from .test_setup import ModuleTestSetUp
from rest_framework import status

class ModuleTests(ModuleTestSetUp):
    def test_everyone_can_list(self):
        res = self.client.get(self.module_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)