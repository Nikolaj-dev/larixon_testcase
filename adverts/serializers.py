from rest_framework import serializers
from .models import Advert


class AdvertSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='city.name')
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Advert
        fields = '__all__'


