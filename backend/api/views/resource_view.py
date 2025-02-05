from ..models import Resource, Subscription
from ..serializers.resource_serializer import ResouceSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

class ResourceViewSet(viewsets.ModelViewSet):
    serializer_class = ResouceSerializer

    # Admins can see all resources
    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Resource.objects.all()
        
        if user.IsAuthenticated:
            subscribed_categories = Subscription.objects.filter(
                user=user, is_active=True
            ).values_list('category_id', flat=True)
            return Resource.objects.filter(module__category_id__in=subscribed_categories)
        
        return Resource.objects.none()
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsAdminUser()]