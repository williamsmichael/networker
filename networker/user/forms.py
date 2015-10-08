from django import forms
from django.contrib.auth.models import User

from .models import NetworkerUser

class UserForm(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:

		model = User
		fields = ('username', 'email', 'password')

class NetworkerUserForm(forms.ModelForm):

	class Meta:

		model = NetworkerUser
		fields = ('date_of_birth', 'profile_image')