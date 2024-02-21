
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# from catalogue.views import getCategory



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('client.urls')),
    # path('accounts/', include("django.contrib.auth.urls")),
    # path('', getCategory, name = "get-category"),
    path('accounts/', include('accounts.urls')),
    path('api/catalogue/', include('catalogue.api.urls')),
    
    path('dashboard/', include("dashboard.urls")),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
