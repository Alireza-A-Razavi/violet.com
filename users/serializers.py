from rest_framework import serializers
from .models import User, ProducerProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username' , 'password')
        extra_kwargs = {'password' : {'required':True, 'write_only':True}}

class ProducerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProducerProfile
        fields = ('profile_pic', 'gender', 'is_selling')
        
