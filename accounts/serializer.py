from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from accounts.models import *
from rest_framework.response import Response
from rest_framework import status




class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'phone')

    def create(self, validated_data):
        user = User.objects.create_user(
            username= validated_data['username'],
            email= validated_data['email'],
            password= validated_data['password'],
            first_name= validated_data['first_name'],
            last_name= validated_data['last_name'],
            phone= validated_data['phone'],
            role= 'CUSTOMER'
        )
        return user

class HostRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostRequest
        fields = ('id','citizen_id_number', 'bank_account', 'address','status','created_at', 'reviewed_at', 'note')

# validate_<field_name>() chỉ kiểm tra 1 field cụ thể
# validate(self, attrs) kiểm tra cả object
    def validate_citizen_id_number(self, value): # tên hàn validate field phải = validate_<tên field cần validate>
        if HostProfile.objects.filter(citizen_id_number = value,).exists():
            raise serializers.ValidationError('CCCD đã được sử dụng')
        return value

    def create(self, validated_data):
        user = self.context['request'].user
        host_request = HostRequest.objects.create(user=user, **validated_data)
        return host_request
    
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields  = '__all__'
    
