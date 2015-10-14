""" group app URL Configuration """

from django.conf.urls import patterns, url

from . import views


urlpatterns = [


    # ------------------------------------------------------------user general
    url(r'^$', views.UserListing.as_view(template_name='user/user_list.html'), name='user_listing'),


    # -------------------------------------------------------------user update
    # url(r'^(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.UserDetail, name='user_detail'),
    url(r'^(?P<pk>[0-9]+)/update/additional$',
        views.UserUpdateAdditional.as_view(template_name='user/user_form.html'), name='update_additional'),
    url(r'^(?P<pk>[0-9]+)/update/main$', views.UserUpdateMain.as_view(
        template_name='user/user_form.html'), name='update_main'),
    url(r'^(?P<pk>[0-9]+)/update/membership$', views.UserUpdateMembership.as_view(
        template_name='user/user_form.html'), name='update_membership'),


    # ---------------------------------------------------------category update
    url(r'^(?P<pk>[0-9]+)/update/phone$', views.UserUpdatePhone.as_view(
        template_name='user/user_form.html'), name='update_phone'),
    url(r'^(?P<pk>[0-9]+)/update/email$', views.UserUpdateEmail.as_view(
        template_name='user/user_form.html'), name='update_email'),
    url(r'^(?P<pk>[0-9]+)/update/address$', views.UserUpdateAddress.as_view(
        template_name='user/user_form.html'), name='update_address'),


    # -------------------------------------------------------categories create
    url(r'^(?P<pk>[0-9]+)/create/phone$', views.CreatePhone.as_view(
        template_name='user/user_form.html'), name='create_phone'),
    url(r'^(?P<pk>[0-9]+)/create/email$', views.CreateEmail.as_view(
        template_name='user/user_form.html'), name='create_email'),
    url(r'^(?P<pk>[0-9]+)/create/address$', views.CreateAddress.as_view(
        template_name='user/user_form.html'), name='create_address'),


    # --------------------------------------------------------instances delete
    url(r'^(?P<pk>[0-9]+)/delete/phone$', views.DeletePhone.as_view(
        template_name='user/user_confirm_delete.html'), name='delete_phone'),
    url(r'^(?P<pk>[0-9]+)/delete/email$', views.DeleteEmail.as_view(
        template_name='user/user_confirm_delete.html'), name='delete_email'),
    url(r'^(?P<pk>[0-9]+)/delete/address$', views.DeleteAddress.as_view(
        template_name='user/user_confirm_delete.html'), name='delete_address'),


    # ------------------------------------------------------------------unused
    # url(r'^(?P<pk>[0-9]+)/delete/$',
    #     views.UserDelete.as_view(), name='delete'),
    # url(r'^$', views.user_listing, name='user_listing'),
    # url(r'^detail/(?P<pk>[0-9]+)/$', views.user_detail, name='user_detail'),
    # url(r'^edit/(?P<pk>\d+)/$', views.UpdateContactView.as_view(),
    # 	name='contacts-edit',),
    # url(r'^detail/main/(?P<pk>[0-9]+)/$', views.user_detail_main, name='user_detail_main'),
    # url(r'^detail/main/(?P<pk>[0-9]+)/edit/$', views.user_detail_main_edit, name='user_detail_main_edit'),
    # url(r'^profile', views.user_new, name='user_new'),
    # url(r'^profile/(?P<pk>[0-9]+)/edit/$', views.user_edit, name='user_edit')

]
