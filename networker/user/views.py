from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import NetworkerUser, UserEmail

# Create your views here.
def user_list(request):

	users = NetworkerUser.objects.all()
	# import pdb; pdb.set_trace()
	return render(request, 'user/user_list.html', {'users': users})

# UserEmail._meta.get_field('user_id').rel.to
# UserEmail._meta.get_field('user_id').rel.to.__name
