from rest_framework import serializers

from core.models import City, Suburb, Region, Property


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ('id', 'name')
        read_only_fields = ('id', 'name')


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id', 'name', 'region')
        read_only_fields = ('id', 'name', 'region')


class SuburbSerializer(serializers.ModelSerializer):

    class Meta:
        model = Suburb
        fields = ('id', 'name', 'city')
        read_only_fields = ('id', 'name', 'city')


class PropertySerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)
    region_id = serializers.IntegerField(write_only=True)
    city = CitySerializer(read_only=True)
    city_id = serializers.IntegerField(write_only=True)
    suburb = SuburbSerializer(read_only=True)
    suburb_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Property
        fields = '__all__'
        read_only_fields = ('id',)
