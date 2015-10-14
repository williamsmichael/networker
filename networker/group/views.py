from django.shortcuts import render
# from django.contrib.auth.models import User, Group

from .models import NetworkerGroup, Group


def group_listing(request):

    groups = NetworkerGroup.objects.all()
    # group = NetworkerGroup.objects.get(group_extension__name="Synergy Consultants, LLC")
    # users = group.group_extension.user_set.all()
    # print(users)

    # import pdb; pdb.set_trace()

    return render(request, 'group/networkergroup_list.html', {'groups': groups})
