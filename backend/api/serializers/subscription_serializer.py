from rest_framework import serializers
from ..models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Subscription
        fields = ['id', 'user', 'category', 'category_name', 'start_date', 'end_date', 'is_active']
        read_only_fields = ['id', 'start_date', 'is_active', 'end_date']

    # User doesn't subscribe to same category twice
    def validate(self, data):
        user = data['user']
        category = data['category']

        if Subscription.objects.filter(user=user, category=category, is_active=True).exists():
            raise serializers.ValidationError("Already subscribed to this category")
        return data
    