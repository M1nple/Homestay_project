from rest_framework import serializers
from accounts.models import *


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'phone')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    

class HostRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostRequest
        fields = ('citizen_id_number', 'bank_account', 'address', 'note')

    def create(self, validated_data):
        user = self.context['request'].user
        host_request = HostRequest.objects.create(user=user, **validated_data)
        return host_request
    
