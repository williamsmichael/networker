from django.shortcuts import render
# from django.contrib.auth.models import User, Group

from .models import NetworkerUser


def user_list(request):

	users = NetworkerUser.objects.all()
	return render(request, 'user/user_list.html', {'users': users})


