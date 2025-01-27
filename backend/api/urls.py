from rest_framework.routers import DefaultRouter
from .views.user_view import UserViewSet
from .views.category_view import CategoryViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'category', CategoryViewSet, basename='category')

urlpatterns = [
    
]+router.urls
