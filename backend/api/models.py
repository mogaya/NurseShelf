from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# Module Model
class Module(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='modules')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.name}"
    
# Resource Model
class Resource(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="resources")
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='notes/')
    is_revision = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({'Revision' if self.is_revision else "Notes" })"

# Subscription Model
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subscriptions')
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} -> {self.category.name} (Active: {self.is_active})"
    