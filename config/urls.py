from django.contrib import admin
from django.urls import path, include
from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('', views.index),
    path('common/', include('common.urls')),
]

handler404 = 'common.views.page_not_found'
