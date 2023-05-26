from .models import UserModel
from rest_framework import serializers

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model= UserModel
#         fields="__all__"


class GetDataSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = UserModel
        fields = ['email','id']