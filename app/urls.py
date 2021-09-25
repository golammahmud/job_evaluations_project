
from django.urls import path,include
from app.views import LoginView,LogoutView,RegisterView,UserInputView,testforms
urlpatterns = [
    # path('home',Home ,name='home' ),
    path('login',LoginView ,name='login'  ),
    path('logout/',LogoutView ,name='logout' ),
    path('registration/',RegisterView ,name='register' ),
    path('',UserInputView ,name='userinput' ),
    path('home/',testforms,name='home'),
]
