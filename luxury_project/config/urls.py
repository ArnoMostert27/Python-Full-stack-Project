"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import create_admin_emergency  # Added this import

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # --- EMERGENCY ADMIN TRIGGER ---
    # Visit this URL once in your browser after pushing to Vercel
    path('make-me-admin-123/', create_admin_emergency),
    
    path('', include('users.urls')),
    path('vehicles/', include('vehicles.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)