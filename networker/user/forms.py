from django import forms
from django.contrib.auth.models import User

from user.models import NetworkerUser

class UserForm(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:

		model = User
		fields = ('username', 'email', 'password')

class NetworkerUserForm(forms.ModelForm):

	class Meta:

		model = NetworkerUser
		fields = ('website', 'profile_image',)