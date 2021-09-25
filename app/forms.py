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
	def clean_email(self):
		email=self.cleaned_data['email']
		print(email)
		if '.@gmail.com' not in email  :
			raise ValidationError('Email is Invalid')
		return email

	def clean(self):
		data=self.cleaned_data
		username=data.get('username')
		password1=data.get('password1')
		password2=data.get('password2')
		users=User.objects.filter(username__icontains=username)
		if users.exists():
			raise ValidationError('users already exists')
		if len(username)< 5:
			raise ValidationError('username is too short')
		if password1 != password2:
			raise ValidationError('password does not match')
		return data

     
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user   





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
     
	
    