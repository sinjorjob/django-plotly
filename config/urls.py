from django.contrib import admin
from django.urls import path, include   #修正

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
]
