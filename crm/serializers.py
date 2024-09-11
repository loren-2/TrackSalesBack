from rest_framework import serializers

from crm.models import User
from crm.models import Company
from crm.models import Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'role')
        extra_kwargs = {'id': {'read_only': True}}


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}
