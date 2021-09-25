from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, NewUserForm, UserInputForm,TestUserInputForm
from django.contrib import messages
from django.conf import settings
from .models import UserInput
import datetime


#User Inputs Views
@login_required(login_url="login")
def testforms(request):
    forms=TestUserInputForm(request.POST or None)
    results=''
    if forms.is_valid():
        number = forms.cleaned_data.get("input_values")
        search_value = forms.cleaned_data.get("search_values")
       
        
        new_search_value=str(search_value) #convert search value integers to strings
        
        num = [int(i) for i in number.split(",")]#convert number strings to list for sorting
        
        user_input = sorted(num, reverse=True) #descending order of user input

        string = [str(i) for i in user_input]
   
        result = str(",".join(string))
        
        
           #finding Inputs value match or not in search_values
        if new_search_value in result:
            results='True'
        else:
            results='False'
        print(f'results:{results}')
        time=datetime.datetime.now()
        save_input = UserInput.objects.create(user=request.user, number=result ,created_at=time )#save the sorted results into database
        messages.success(request, message="data saved successfully")
    forms=TestUserInputForm(request.POST or None)
    return render(request,template_name='index.html' , context={'form':forms ,'result':results})
    



#User Inputs Views
@login_required(login_url="login")
def UserInputView(request):
    test=TestUserInputForm(request.POST or None)
    form = UserInputForm(request.POST)#get form value from userinput forms
    results=''
    if form.is_valid():
        number = form.cleaned_data.get("input_values")
        search_value = form.cleaned_data.get("search_values")
        print(f'number_value{type(number)}')
        
        
        
        print(f'search_value{type(search_value)}')
        new_search_value=str(search_value) #convert search value integers to strings
        
        
        
        print(f'new_search_value{type(new_search_value)}')
        
        
        
     
        num = [int(i) for i in number.split(",")]#convert number strings to list for sorting
        
        user_input = sorted(num, reverse=True) #descending order of user input

        string = [str(i) for i in user_input]
   
        result = str(",".join(string))
        print(f'result:{result}')
        
      #finding Inputs value match or not in search_values
        if new_search_value in result:
            results='True'
        else:
            results='False'
            
            
        time=datetime.datetime.now()
        # save_input = UserInput.objects.create(user=request.user, number=result ,created_at=time )#save the sorted results into database
   
        messages.success(request, message="data saved successfully")
    form = UserInputForm()
    return render(request, template_name="userforms.html", context={"form": form,'results':results ,'test':test})



#login view
def LoginView(request):
    if request.user.is_authenticated:
        messages.info(request, message=f"you are already logged in {request.user.username} ")
        return redirect("userinput")
    else:
        form = LoginForm(request.POST)
      
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            messages.warning(request, message="login failed")
        else:
            form = LoginForm()
    return render(request, template_name="login.html", context={"form": form})


#logout view
@login_required
def LogoutView(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, f"You have been successfully logged out  {request.user.username} ")
        return redirect("login")
    return render(request, template_name="logout.html")



#register view
def RegisterView(request):
    form = NewUserForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, message="Your Registration successfully Done")
        return redirect("login")
    else:
        form = NewUserForm()
    return render(request, template_name="registration.html", context={"form": form})
