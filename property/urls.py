from django.urls import path, include
from rest_framework.routers import DefaultRouter

from property import views


router = DefaultRouter()
router.register('regions', views.RegionViewSet)
router.register('cities', views.CityViewSet)
router.register('suburbs', views.SuburbViewSet)
router.register('properties', views.PropertyViewSet)


app_name = 'property'


urlpatterns = [
    path('', include(router.urls))
]
