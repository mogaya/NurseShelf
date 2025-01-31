from ..models import Resource
from rest_framework import serializers

class ResouceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id','module', 'title', 'description', 'file', 'is_revision', 'created_at']
        read_only_fields = ['id', 'created_at']