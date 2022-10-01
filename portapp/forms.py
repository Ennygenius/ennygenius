from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	
	Type_Your_Message= forms.CharField(widget= forms.Textarea)


	class meta:
		fields = [
			'username',
			'email',
			'Type_Your_Message'
			

		]