from dataclasses import field
import email
from multiprocessing import Value
from pyexpat import model
from rest_framework import serializers
from accounts.models import *
from rest_framework.response import Response
from rest_framework import status


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'phone')
    
    def validate_email(self, value):
        if User.objects.filter(email = value).exists():
            raise serializers.ValidationError('Email đã được sử dụng')
        return value

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
        fields = (
            'id', 
            'citizen_id_number', 
            'bank_account', 
            'address', 
            'status', 
            'created_at', 
            'reviewed_at', 
            'note'
            )

# validate_<field_name>() chỉ kiểm tra 1 field cụ thể
# validate(self, attrs) kiểm tra cả object
    def validate_citizen_id_number(self, value): # tên hàn validate field phải = validate_<tên field cần validate>
        if HostProfile.objects.filter(citizen_id_number = value,).exists():
            raise serializers.ValidationError('CCCD đã được sử dụng')
        return value

    def validate(self, data):
        user = self.context['request'].user
        # đã có request đang PENDING
        exists = HostRequest.objects.filter(
            user=user,
            status='PENDING'
        ).exists()
        if exists:
            raise serializers.ValidationError(
                "Bạn đã gửi yêu cầu trở thành host và đang chờ duyệt."
            )
        # host request
        if user.role == 'HOST':
            raise serializers.ValidationError("bạn đã là host")
        return data

    def create(self, validated_data):
        user = self.context['request'].user
        host_request = HostRequest.objects.create(user=user, **validated_data)
        return host_request
    
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields  = '__all__'
    
