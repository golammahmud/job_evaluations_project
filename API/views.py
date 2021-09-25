from django.shortcuts import render
from .serializers import UserInputSerializers,UserSerializer
from rest_framework import viewsets
from app.models import UserInput
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

#..........i used jwt token based authenications globally in setting.py................


# all userinputs view api
class UserInputView(viewsets.ModelViewSet):
    queryset=UserInput.objects.all()
    serializer_class=UserInputSerializers

 
# all user based inputs view   
class UserBasedInputView(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
 