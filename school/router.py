from rest_framework import routers
from .views import (CompteViewList, 
					UserViewSet,PermissionViewSet,  ContentTypeViewSet, GroupViewSet)

#Creation des routes des API des models
router = routers.DefaultRouter()

router.register('comptes', CompteViewList)
router.register('users', UserViewSet)
router.register('permissions', PermissionViewSet)
router.register('contenttypes', ContentTypeViewSet)
router.register('groups', GroupViewSet)