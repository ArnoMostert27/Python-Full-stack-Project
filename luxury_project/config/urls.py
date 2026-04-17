"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # We removed the 'make-me-admin-123' path because 
    # the new index.py handles user creation automatically.
    
    path('', include('users.urls')),
    path('vehicles/', include('vehicles.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)