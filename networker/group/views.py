from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.db.models import Count

from .models import NetworkerGroup, Group


# ---------------------------------------------------------------------listing
@login_required
def listing_group(request):
	# get the groups for the login user

	# query auth group(s) for login user
	user_groups = Group.objects.all().filter(user=request.user)

	# get the ids for the auth groups of the login user
	id_list = []
	name_list = []
	for attribute in user_groups:

		id_list.append(attribute.id)
		name_list.append(attribute.name)

	# query the extended networkergroup details by id or pk
	group_list = NetworkerGroup.objects.all().prefetch_related().filter(pk__in=id_list)

	print("group list:", group_list)

	member_count_list = []
	# print("name list: ", name_list)
	for name in name_list:

		# member_count = {}

		# name = name
		total = User.objects.filter(groups__name=name).count()
		
		# member_count = {
			# 'name': name,
			# 'total': total
		# }

		member_count_list.append(total)

	# data = [group_list, member_count_list]

	# print(member_count_list)
	return render(request, 'group/group_list.html', {'group_list': group_list})
	# return render(request, 'group/group_list.html', {'data': data})
    

# ----------------------------------------------------------------------unused
# class ListingGroup(ListView):
#     """ List of all groups for a login user """
#     model = NetworkerGroup

# @login_required
# def listing_group(request):
# 	""" List of all group(s) for the login user """
# 	groups = NetworkerGroup.objects.all()
# 	# group = NetworkerGroup.objects.get(group_extension__name="Synergy Consultants, LLC")
#     # users = group.group_extension.user_set.all()
#     # print(users)

#     # import pdb; pdb.set_trace()

# 	return render(request, 'group/group_list.html', {'groups': groups})


# def test1(request):
# 	current_user = request.user
# 	membership = User.objects.get(pk=current_user.pk)
# 	groups = membership.groups.all()

# 	print(groups)
# 	# return HttpResponse("test")
	# return render(request, 'group/test.html', {'membership': membership})
