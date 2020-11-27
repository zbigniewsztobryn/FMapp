from rest_framework.routers import DefaultRouter
from .views import ContactsViewSet, DataViewSet,PropertiesViewSet
router = DefaultRouter()
router.register('contacts', ContactsViewSet)
router.register('data', DataViewSet)
router.register('properties', PropertiesViewSet)