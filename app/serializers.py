from rest_framework import serializers
from app.models import *


class EmployeeSerilizaers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
                    'id',
                    'first_name',
                    'last_name',
                    'about_me',
                    'joined_at',
                    'partner'
                ]
    

class TeamSerliazers(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class SectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = [
                'id',
                'sector_name',
                'location'
        ]


class ManagerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Manager
        field = "__all__"