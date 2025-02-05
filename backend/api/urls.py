from rest_framework.routers import DefaultRouter
from .views import user_view, category_view, module_view, resource_view, subscription_view

router = DefaultRouter()
router.register(r'user', user_view.UserViewSet, basename='user')
router.register(r'category', category_view.CategoryViewSet, basename='category')
router.register(r'module', module_view.ModuleViewSet, basename='module')
router.register(r'resource', resource_view.ResourceViewSet, basename='resource')
router.register(r'subscription', subscription_view.SubscriptionViewSet, basename='subscription')

urlpatterns = [
    
]+router.urls
