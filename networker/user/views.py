from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import NetworkerUser

users = User.objects.all()

# Create your views here.
def user_list(request):
	networker_users = User.objects.all()

	# # httpResponse method without templates
	# output = ', '.join([str(networker_user) for networker_user in networker_users])
	# return HttpResponse(output)

	return render(request, 'user/user_list.html', {'networker_users': networker_users})