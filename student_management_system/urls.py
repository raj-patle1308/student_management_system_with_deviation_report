from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView
from student_management_system import settings
from student_management_app import views  # Import your custom admin dashboard view

urlpatterns = [
    path('django_admin/', admin.site.urls), 
    path('admin/', admin.site.urls),
    path('', include('student_management_app.urls')),  # Include app-specific URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
