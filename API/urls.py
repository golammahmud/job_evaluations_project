from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import UserInputView,UserBasedInputView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView



router=routers.DefaultRouter()
router.register('all-userinputs',UserInputView)
router.register('user-based-inputs',UserBasedInputView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/',include('rest_framework.urls')),
    path('get_token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #get token 
    path('token_refresh/', TokenRefreshView.as_view(), name='token_refresh'),# get refresh token
    

]