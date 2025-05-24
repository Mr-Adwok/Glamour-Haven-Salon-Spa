from rest_framework import serializers
from .models import CustomUser


class SignUp_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['full_name','email','phone','password']


    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            password=validated_data['password'],
            phone=validated_data['phone'],
            full_name=validated_data['full_name']

        )
        user.set_password(validated_data['password'])
        user.save()
        return user