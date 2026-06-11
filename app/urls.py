from django.urls import path
from .views import *
urlpatterns = [
    path('employee/',EmployeeListCreateView.as_view(), name='list-employee'),
    path('employee/<int:pk>/',EmployeeListCreateView.as_view(), name='list-employee-by-id'),
    path('manager/', ManagerListCreateView.as_view(), name="list-managers"),
    path('manager/<int:pk>/',ManagerListCreateView.as_view(), name='list-instructor-by-id'),
    path('sector/', SectorListCreateView.as_view(), name='list-sectors'),
    path('sector/<int:pk>/', SectorListCreateView.as_view(), name='list-sector-by-id')
] 