from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from app import views

from .yasg import schema_view

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("admin/", admin.site.urls),
]

urlpatterns1 = [
    path("", include('app.urls')),
    path("lockout/", views.lockout_view, name='lockout_url'),
]

urlpatterns += i18n_patterns(
    path('', include(urlpatterns1)),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


