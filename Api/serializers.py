from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework import permissions
from .models import *

class ManagerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if Employee.objects.filter(user=request.user).role == 'manager':
            return True
        else:
            return False

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        read_only_fields = ('user_ptr',)
        fields = '__all__'
        permission_classes = [IsAuthenticated]
        authentication_classes = [TokenAuthentication]

class BagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bag
        fields = '__all__'
        permission_classes = [permissions.AllowAny]