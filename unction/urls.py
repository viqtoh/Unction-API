from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from unction import settings
from .router import router
from rest_framework.authtoken import views

admin.site.site_header = "Admin"
admin.site.site_title = "Blog Portal"
admin.site.index_title = "Settings"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('MainApi.urls') ),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)