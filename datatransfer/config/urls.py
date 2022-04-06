"""datatransfer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar

#from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView  # 追加
from io_gcs.views import HealthcheckView


urlpatterns = [
    # admin
    #path('admin/', admin.site.urls),
    # debug toolbar
    path('__debug__/', include(debug_toolbar.urls)),
    # apps
    path('', include('io_gcs.urls')),
    # docs
    path('docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('healthcheck/', HealthcheckView.as_view(), name='healthcheck'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
