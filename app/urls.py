from django.contrib import admin
from django.urls import path, include

from core.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='home'),
]
