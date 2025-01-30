from rest_framework import viewsets
from ..serializers.module_serializer import ModuleSerializer
from ..models import Module
from rest_framework.permissions import AllowAny, IsAdminUser

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]
