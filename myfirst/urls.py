
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('articles/', include('articles.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
]
