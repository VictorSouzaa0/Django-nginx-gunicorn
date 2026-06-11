from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.generics import ListCreateAPIView,DestroyAPIView
from .serializers import TeamSerliazers, EmployeeSerilizaers, ManagerSerializers, SectorSerializers
from .models import Team, Employee, Manager, Sector

class EmployeeListCreateView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerilizaers
    permission_classes = [AllowAny]

class EmployeeListDestroyView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerilizaers
    permission_classes = [AllowAny]



class TeamListCreateView(ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerliazers
    permission_classes = [AllowAny]

class TeamDestroyView(DestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerliazers
    permission_classes = [AllowAny]


class SectorListCreateView(ListCreateAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializers
    permission_classes = [AllowAny]

class SectorDestroyView(DestroyAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializers
    permission_classes = [AllowAny]


class ManagerListCreateView(ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializers
    permission_classes = [AllowAny]