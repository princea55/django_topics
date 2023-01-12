from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from django_topics import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.forms.urls'), name='forms'),
    path('', include('web.user.urls'), name='forms')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)