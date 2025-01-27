# from rest_framework import generics

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from ..serializers.user_serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

# Create your views here.

# User ViewSet
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return [IsAdminUser()]
