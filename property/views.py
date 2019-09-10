
import logging
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (BasePermission,
                                        IsAuthenticated, SAFE_METHODS)

from core.models import Region, City, Suburb, Property
from property import serializers


logger = logging.getLogger(__name__)


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class RegionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RegionSerializer
    queryset = Region.objects.all()


class CityViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CitySerializer
    queryset = City.objects.all()


class SuburbViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SuburbSerializer
    queryset = Suburb.objects.all()


class PropertyViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PropertySerializer
    queryset = Property.objects.select_related(
        'region', 'city', 'suburb').all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated | ReadOnly, )

    def get_queryset(self):
        """Should set filter here """
        queryset = Property.objects.select_related(
        'region', 'city', 'suburb').all()

        propertyType = self.request.query_params.get('propertyType')
        region = int(self.request.query_params.get('region')
                     ) if self.request.query_params.get('region') else 0
        city = int(self.request.query_params.get('city')
                   ) if self.request.query_params.get('city') else 0
        suburb = int(self.request.query_params.get('suburb')
                     ) if self.request.query_params.get('suburb') else 0

        if propertyType:
            queryset = queryset.filter(propertyType=propertyType)

        if region > 0:
            queryset = queryset.filter(region=region)

        if city > 0:
            queryset = queryset.filter(city=city)

        if suburb > 0:
            queryset = queryset.filter(suburb=suburb)

        return queryset

    # def perform_create(self, serializer):
    #     """Create a new Property"""
    #     serializer.save(user=self.request.user)
