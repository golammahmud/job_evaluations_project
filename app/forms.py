from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from  .models import UserInput

# Create your forms here.

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150,widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password'}))
    



class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
	def clean(self):
		data=self.cleaned_data
		username=data.get("username")
		password1=data.get("password")
		password2=data.get("password1")
		user=User.objects.filter(username=username)
		if user.exists():
			raise ValidationError(message='username already')
      

		if password1 ==password2:
			raise ValidationError(message='password does not match')
		return data
  
     
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user   

class UserInputForm(forms.Form):
	input_values=forms.CharField(label=('Input values'))
	search_values=forms.IntegerField(label=('Search values'))


class TestUserInputForm(forms.Form):
	input_values=forms.CharField(label=('Input values'))
	search_values=forms.IntegerField(label=('Search values'))
	def clean_input_values(self):
		inputs=self.cleaned_data['input_values']
		print(inputs)
		if '.'  in inputs  :
			raise ValidationError('floating value  is not allowed')
		return inputs
	def clean_search_values(self):
		values=self.cleaned_data['search_values']
		if values<0:
			raise ValidationError('less than 0 value is not acceptable')
		return values 
     
	
    