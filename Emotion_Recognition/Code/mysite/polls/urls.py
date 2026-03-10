from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import handler, uploading

urlpatterns = [
    path('', handler, name='homepage'),
    path('upload/', uploading, name='upload')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)