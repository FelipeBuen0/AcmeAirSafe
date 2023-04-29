from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics,  permissions
from .serializers import EmployeeSerializer, BagSerializer
from .models import Bag, Employee
class ManagerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if Employee.objects.filter(user=request.user).role == 'manager':
            return True
        else:
            return False

class BagListView(generics.ListCreateAPIView):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class BagRetrieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class EmployeeListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    class BagListView(generics.ListCreateAPIView):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class LoadListView(generics.ListCreateAPIView):
    queryset = Load.objects.all()
    serializer_class = LoadSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class LoadRetrieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Load.objects.all()
    serializer_class = LoadSerializer

class LocationListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer