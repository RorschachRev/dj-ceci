from django import forms
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password', 'first_name', 'last_name', 'email')
	
class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('company_name',)

