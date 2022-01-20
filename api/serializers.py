from rest_framework import serializers
from .models import Employee

class EmpSerializer(serializers.Serializer):
	name=serializers.CharField(max_length=200)
	email=serializers.EmailField(max_length=200)
	position=serializers.CharField(max_length=200)

	def create(self,validate_data):
		return Employee.objects.create(**validate_data)