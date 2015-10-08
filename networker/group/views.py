from django.shortcuts import render
from django.contrib.auth.models import User, Group

from .models import NetworkerGroup, Group


def group_list(request):

	groups = NetworkerGroup.objects.all()
	# users = groups.user_set.all()

	# import pdb; pdb.set_trace()

	return render(request, 'group/group_list.html', {'groups': groups})