from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import NetworkerUser

# Create your views here.
def user_list(request):
	# users = User.objects.all()
	users = NetworkerUser.objects.all()
	# import pdb; pdb.set_trace()
	return render(request, 'user/user_list.html', {'users': users})