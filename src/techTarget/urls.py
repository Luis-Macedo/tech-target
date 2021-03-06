
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/login/', include('login.urls')),
    path('api/form/', include('forms.urls')),
    path('api/dashboards/', include('dashboards.urls')),
]
