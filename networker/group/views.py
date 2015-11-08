from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.core.urlresolvers import reverse
from django.db.models import Count


from .models import NetworkerGroup
from user.models import NetworkerUser


#----------------------------------------------------------------group profile
@login_required
def GroupProfile(request, pk):
	""" Details of a group """

	profile = get_object_or_404(NetworkerGroup, pk=pk)
	return render(request, 'group/group_profile.html', {'profile': profile})


# ---------------------------------------------------------------------listing
@login_required
def listing_group(request):
	""" List of all group for a login user """

	# query request.user membership_list
	login_user = NetworkerUser.objects.get(pk=request.user.id)
	group_list = login_user.membership_list.all().prefetch_related()

	# print(login_user)
	# print(group_list)

	id_list = []
	# for each_group in group_list:
		# print(each_group.pk, each_group)

	return render(request, 'group/group_list.html', {"group_list": group_list})


# ----------------------------------------------------------------------update
class GroupUpdateAbout(UpdateView):
    """ Update auth-group details for a login user group """
    model = NetworkerGroup
    fields = '__all__'
    # success_url = '.'
    section = "About"
    title = 'update'
    button = 'Update'

    def get_success_url(self):
        return reverse('update_about_group', kwargs={
            'pk': self.object.pk,
        })


# ----------------------------------------------------------------------unused
# class GroupUpdateAdditional(UpdateView):
#     """ Update networker details for a login user group """
#     model = NetworkerGroup
#     fields = '__all__'
#     # success_url = '.'
#     section = "Additional"
#     title = 'update'
#     button = 'Update'

#     def get_success_url(self):
#         return reverse('update_additional_group', kwargs={
#             'pk': self.object.pk,
#         })
        
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
