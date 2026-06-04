from rest_framework import serializers
from app.models import *


class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
    

class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"