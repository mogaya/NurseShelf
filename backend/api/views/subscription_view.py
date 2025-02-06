from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils.timezone import now, timedelta
from ..models import Subscription
from ..serializers import subscription_serializer

"""
custom permission
- Admins can view n manage all subscriptions
- Users can only see n manage their own subscriptions
"""
class IsAdminOrOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user == request.user

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = subscription_serializer.SubscriptionSerializer
    permission_classes = [IsAdminOrOwner]

    """
    - Admins: see all subscriptions
    - Users: See only their own subscriptions
    """
    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Subscription.objects.all()
        return Subscription.objects.filter(user=self.request.user, is_active=True)
    
    # setting user and subscription duration
    def perform_create(self, serializer):
        end_date = now().date() + timedelta(days=365.25/2)
        serializer.save(user=self.request.user, end_date=end_date)

    # Allowing users to cancel own subscription, Admin can cancel any subscription
    @action(detail=True, methods=['POST'])
    def cancel(self, request, pk=None):
        # print(f"Cancel action called for subscription ID: {pk}")
        subscription = self.get_object()

        if not request.user.is_staff and subscription.user != request.user:
            return Response({"error": "You can only cancel your own subscription"}, status=status.HTTP_403_FORBIDDEN)
        
        subscription.is_active = False
        subscription.save()
        return Response({"message": "Subscription canceled successfully"})
