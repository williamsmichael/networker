""" group app URL Configuration """

from django.conf.urls import url

from . import views

urlpatterns = [

	# ----------------------------------------------------------------listview
    url(r'^$', 'group.views.listing_membership', name='listing_membership'),


    # ------------------------------------------------------------------unused
    # url(r'^$', views.listing_group, name='listing_group'),

]

