from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.core.urlresolvers import reverse
from django.db.models import Count


from .models import Group, NetworkerGroup
from user.models import NetworkerUser


#----------------------------------------------------------------group profile
@login_required
def GroupProfile(request, pk):
	""" Details of a group """

	membership = get_object_or_404(NetworkerGroup, pk=pk)
	return render(request, 'group/group_profile.html', {'membership': membership})


# ---------------------------------------------------------------------listing
@login_required
def listing_group(request):
	""" List of all group for a login user """

	# query request.user membership_list
	login_user = NetworkerUser.objects.get(pk=request.user.id)
	group_list = login_user.membership_list.all().prefetch_related()
	print(group_list)

	# # get the ids for the auth groups of the login user
	# id_list = []
	# name_list = []
	# for attribute in member_group_list:

	# 	id_list.append(attribute.id)
	# 	name_list.append(attribute.name)

	# # query the extended networkergroup details by id or pk
	# group_list = NetworkerGroup.objects.all().prefetch_related().filter(pk__in=id_list)

	# print("group list:", group_list)

	# member_count_list = []
	# # print("name list: ", name_list)
	# for name in name_list:

	# 	# member_count = {}

	# 	# name = name
	# 	total = User.objects.filter(groups__name=name).count()
		
	# 	# member_count = {
	# 		# 'name': name,
	# 		# 'total': total
	# 	# }

	# 	member_count_list.append(total)

	# # data = [group_list, member_count_list]

	# # print(member_count_list)

	# # return render(request, 'group/group_list.html', {'data': data})
	return render(request, 'group/group_list.html', {"group_list": group_list})


# ----------------------------------------------------------------------update
class GroupUpdateMain(UpdateView):
    """ Update auth-group details for a login user group """
    model = Group
    fields = ['name']
    # success_url = '.'
    section = "Main"
    title = 'update'
    button = 'Update'

    def get_success_url(self):
        return reverse('update_main_group', kwargs={
            'pk': self.object.pk,
        })


class GroupUpdateAdditional(UpdateView):
    """ Update networker details for a login user group """
    model = NetworkerGroup
    fields = '__all__'
    # success_url = '.'
    section = "Additional"
    title = 'update'
    button = 'Update'

    def get_success_url(self):
        return reverse('update_additional_group', kwargs={
            'pk': self.object.pk,
        })


# ----------------------------------------------------------------------unused
# class ListingGroup(ListView):
#     """ List of all groups for a login user """
#     model = NetworkerGroup

# @login_required
# def listing_group(request):
# 	""" List of all group(s) for the login user """
# 	groups = NetworkerGroup.objects.all()
# 	# group = NetworkerGroup.objects.get__name="Synergy Consultants, LLC")
#     # users = group.user_set.all()
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
