from rest_framework import serializers
from app.models import UserInput

from django.contrib.auth.models import User



class UserInputSerializers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = UserInput
        fields=['number','created_at']
      


class UserSerializer(serializers.HyperlinkedModelSerializer):
    payload=UserInputSerializers(many=True,read_only=True)# nested serializers 
    class Meta:
        model = User
        fields=['id','username','payload']
        



