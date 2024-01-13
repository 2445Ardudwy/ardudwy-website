from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.website.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = "apps.website.views.pageNotFound"
handler500 = "apps.website.views.serverError"
handler403 = "apps.website.views.permissionDenied"
handler400 = "apps.website.views.badRequest"