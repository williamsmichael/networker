from django import forms
from django.contrib.auth.models import User

from .models import *


class UserForm(forms.ModelForm):
    """ Register Auth-User form """
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class NetworkerUserForm(forms.ModelForm):
    """ Register Networker User form """
    class Meta:
        model = NetworkerUser
        fields = ()


class InviteForm(forms.Form):
    """ Invite user to a group """
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField(required=False)
    message = forms.CharField()


# ----------------------------------------------------------------------unused

# class UserDetailMainForm(forms.ModelForm):
#     """ Update a Networker User section=Main of profile"""
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'first_name', 'last_name',)

#     def __init__(self, *args, **kwargs):
#         self.user = kwargs.pop('user', None)
#         super(UserDetailMainForm, self).__init__(*args, **kwargs)

# class UserNewForm(forms.ModelForm):
#     """ Update a Networker User profile form """
#     class Meta:
#         model = User
#         # fields = '__all__'
#         exclude = ['is_superuser', 'user_permissions', 'is_staff',
#                    'is_active', 'date_joined', 'last_login', 'groups']
