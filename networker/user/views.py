from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import NetworkerUser


def user_list(request):

	users = NetworkerUser.objects.all()
	# import pdb; pdb.set_trace()
	return render(request, 'user/user_list.html', {'users': users})

# def email_list(request, pk):
# 	email = NetworkerUser.objects.get(pk=pk)
# 	# email_list = []
# 	usr = NetworkerUser.objects.get(pk=pk).select_related()
# 	print(usr)

# 	return render(request, 'user/email_list.html', {'email': email, "usr": usr})


