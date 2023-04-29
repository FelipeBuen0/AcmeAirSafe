from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework import permissions
from .models import *
class EmployeeSerializer(serializers.ModelSerializer):
    def create(self, data):
        employee = Employee(name=data['name'],
                            role=data['role'],
                            sector=data['sector'],
                            access_level=data['access_level'],
                            username=data['username'])
        employee.set_password(data['password'])
        employee.save()
        return employee
    class Meta:
        model = Employee
        write_only_fields = ['password']
        read_only_fields = ('user_ptr',)
        fields = ['name',
                  'role',
                  'sector',
                  'access_level',
                  'password',
                  'user_ptr',
                  'username']

class BagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bag
        fields = '__all__'