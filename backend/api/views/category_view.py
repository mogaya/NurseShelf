from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from ..models import Category
from ..serializers.category_serializer import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]