from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User, Group

from .models import NetworkerGroup, Group
# from user.models import NetworkerUser


def test1(request):
	current_user = request.user
	membership = User.objects.get(pk=current_user.pk)
	groups = membership.groups.all()

	print(groups)
	# return HttpResponse("test")
	return render(request, 'group/test.html', {'membership': membership})


@login_required
def listing_user_groups(request):
	# get the groups for the login user
	current_user = request.user
	user_groups = Group.objects.filter(user=request.user).values('networkergroup__welcome_message', 'networkergroup__group_description').distinct()
	# networker_groups = user_groups.annotate(networkergroup)

	print(user_groups)
	# print(networker_groups)

	return render(request, 'group/test.html', {'user_groups': user_groups})
	# return HttpResponse("test")


@login_required
def listing_group(request):
	""" List of all group(s) for the login user """
	groups = NetworkerGroup.objects.all()
	# group = NetworkerGroup.objects.get(group_extension__name="Synergy Consultants, LLC")
    # users = group.group_extension.user_set.all()
    # print(users)

    # import pdb; pdb.set_trace()

	return render(request, 'group/group_list.html', {'groups': groups})
