from .models import Category , City , ads
from rest_framework.serializers import ModelSerializer


class Ads_Serializers(ModelSerializer):
    class Meta:
        model = ads
        fields = '__all__'