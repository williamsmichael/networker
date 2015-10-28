""" group app URL Configuration """

from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [


	# ----------------------------------------------------------------listview
    url(r'^$', 'group.views.listing_group', name='listing_group'),


    # -----------------------------------------------------------group profile
    url(r'^(?P<pk>[0-9]+)/$', views.GroupProfile, name='group_profile'),


    # ------------------------------------------------------------------unused
    # url(r'^$', views.listing_group, name='listing_group'),
	# url(r'^$', login_required(views.ListingGroup.as_view(template_name='group/group_list.html')), name='listing_group'),

]

