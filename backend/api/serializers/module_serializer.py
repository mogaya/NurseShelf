from rest_framework import serializers
from ..models import Module

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'code', 'name', 'description', 'category', 'trending', 'created_at']
        read_only_fields = ['id', 'created_at']