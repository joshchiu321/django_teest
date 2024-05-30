from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from comments.views import comment_view
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from bikeStation.views import BikeStationViewSet



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),


    path('users/', include('users.urls')),
    path('bikeStation/', include('bikeStation.urls')),
    path('comments/', include('comments.urls')),


]
