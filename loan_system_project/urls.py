from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # Keep django admin if needed
    path('api/', include('apps.urls')),
]
