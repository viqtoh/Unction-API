from MainApi.viewsets import userviewsets
from rest_framework import routers
 
router = routers.DefaultRouter()
router.register('user', userviewsets)