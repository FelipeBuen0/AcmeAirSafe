from rest_framework import generics,  permissions
from .serializers import EmployeeSerializer, BagSerializer
from .models import Bag, Employee

class BagListView(generics.ListCreateAPIView):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer

class BagRetrieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer

class EmployeeListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.AllowAny]

class EmployeeRetrieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer