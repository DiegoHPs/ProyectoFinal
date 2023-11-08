from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('FirstApp/', include('FirstApp.urls')),
    path('', lambda request: redirect('logueo', permanent=False)),
]