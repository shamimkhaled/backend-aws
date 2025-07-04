
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Backend Shop API",
      default_version='v1',
      description="Swagger API documentation for the Backend Shop API"
    #   terms_of_service="https://www.google.com/policies/terms/",
    #   contact=openapi.Contact(email="contact@shop.local"),
    #   license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('shop.urls')),
    path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]
