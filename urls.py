from django.contrib import admin
from django.urls import path, include

from app.api.core.views import home

urlpatterns = [
    path('', home, name='home'),
    path('api/', include('app.api.urls')),
    path('admin/', admin.site.urls),
]
