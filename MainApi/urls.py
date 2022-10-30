from django.urls import path, include
from rest_framework import routers
from .import views

router = routers.DefaultRouter()
router.register(r'data',views.DataViewSet)


urlpatterns = [
	path('',include(router.urls)),
	path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
	path('post/<str:username>/<str:password>/<str:firstname>/<str:lastname>/<str:mobile>/<str:address>/<str:state>/<str:country>',views.CreateUser,name='CreateUser'),
	path('login/<str:username>/<str:password>',views.loginView,name='login'),
	path('checklogin/',views.checkAuth,name='checkAuth'),
	path('logout/',views.logoutView,name='logout')
]