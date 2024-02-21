from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Project Api",
        default_version='v1',
        description="Project Api documentations",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email='behruzbotiraliyev@mail.com'),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    url=settings.HOST,
    authentication_classes=(TokenAuthentication, JWTAuthentication),
)
