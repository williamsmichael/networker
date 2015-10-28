""" group app URL Configuration """

from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [


	# ----------------------------------------------------------------listview
    url(r'^$', 'group.views.listing_group', name='listing_group'),


    # -----------------------------------------------------------group profile
    url(r'^(?P<pk>[0-9]+)/$', views.GroupProfile, name='group_profile'),


    # --------------------------------------------------------------updateview
    url(r'^(?P<pk>[0-9]+)/main$', login_required(views.GroupUpdateMain.as_view(template_name='group/create_update_form_group.html')), name='update_main_group'),
    url(r'^(?P<pk>[0-9]+)/additional$', login_required(views.GroupUpdateAdditional.as_view(template_name='group/create_update_form_group.html')), name='update_additional_group'),


    # ------------------------------------------------------------------unused
    # url(r'^$', views.listing_group, name='listing_group'),
	# url(r'^$', login_required(views.ListingGroup.as_view(template_name='group/group_list.html')), name='listing_group'),

]

