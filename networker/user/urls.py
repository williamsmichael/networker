""" group app URL Configuration """

from django.conf.urls import patterns, url

from . import views


urlpatterns = [


    # ----------------------------------------------------------------listview
    url(r'^$', views.ListingUser.as_view(template_name='user/user_list.html'), name='listing_user'),
    url(r'^(?P<pk>[0-9]+)/phone$', views.ListingPhone.as_view(template_name='user/userphone_list.html'), name='listing_phone'),
    url(r'^(?P<pk>[0-9]+)/email$', views.ListingEmail.as_view(template_name='user/useremail_form.html'), name='listing_email'),
    url(r'^(?P<pk>[0-9]+)/address$', views.ListingAddress.as_view(template_name='user/useraddress_form.html'), name='listing_address'),
    url(r'^(?P<pk>[0-9]+)/socialmedia$', views.ListingSocialMedia.as_view(template_name='user/usersocialmedia_form.html'), name='listing_social_media'),
    url(r'^(?P<pk>[0-9]+)/job$', views.ListingJob.as_view(template_name='user/userjob_form.html'), name='listing_job'),
    url(r'^(?P<pk>[0-9]+)/skill$', views.ListingSkill.as_view(template_name='user/userskill_form.html'), name='listing_skill'),


    # ---------------------------------------------------------updateview user
    # url(r'^(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.UserDetail, name='user_detail'),
    url(r'^(?P<pk>[0-9]+)/additional$',
        views.UserUpdateAdditional.as_view(template_name='user/create_update_form.html'), name='update_additional'),
    url(r'^(?P<pk>[0-9]+)/main$', views.UserUpdateMain.as_view(
        template_name='user/create_update_form.html'), name='update_main'),
    url(r'^(?P<pk>[0-9]+)/membership$', views.UserUpdateMembership.as_view(
        template_name='user/create_update_form.html'), name='update_membership'),


    # --------------------------------------------------updateview by category
    url(r'^(?P<pk>[0-9]+)/phone/(?P<phone>[0-9]+)$', views.UserUpdatePhone.as_view(
        template_name='user/create_update_form.html'), name='update_phone'),
    url(r'^(?P<pk>[0-9]+)/email/(?P<email>[0-9]+)$', views.UserUpdateEmail.as_view(
        template_name='user/create_update_form.html'), name='update_email'),
    url(r'^(?P<pk>[0-9]+)/address/(?P<address>[0-9]+)$', views.UserUpdateAddress.as_view(
        template_name='user/create_update_form.html'), name='update_address'),
    url(r'^(?P<pk>[0-9]+)/social_media/(?P<social_media>[0-9]+)$', views.UserUpdateSocialMedia.as_view(
        template_name='user/create_update_form.html'), name='update_social_media'),
    url(r'^(?P<pk>[0-9]+)/job/(?P<job>[0-9]+)$', views.UserUpdateJob.as_view(
        template_name='user/create_update_form.html'), name='update_job'),
    url(r'^(?P<pk>[0-9]+)/skill/(?P<skill>[0-9]+)$', views.UserUpdateSkill.as_view(
        template_name='user/create_update_form.html'), name='update_skill'),


    # --------------------------------------------------------------createview
    url(r'^(?P<pk>[0-9]+)/phone/create$', views.CreatePhone.as_view(
        template_name='user/create_update_form.html'), name='create_phone'),
    url(r'^(?P<pk>[0-9]+)/email/create$', views.CreateEmail.as_view(
        template_name='user/create_update_form.html'), name='create_email'),
    url(r'^(?P<pk>[0-9]+)/address/create$', views.CreateAddress.as_view(
        template_name='user/create_update_form.html'), name='create_address'),
    url(r'^(?P<pk>[0-9]+)/social_media/create$', views.CreateSocialMedia.as_view(
        template_name='user/create_update_form.html'), name='create_social_media'),
    url(r'^(?P<pk>[0-9]+)/job/create$', views.CreateJob.as_view(
        template_name='user/create_update_form.html'), name='create_job'),
    url(r'^(?P<pk>[0-9]+)/skill/create$', views.CreateSkill.as_view(
        template_name='user/create_update_form.html'), name='create_skill'),


    # ------------------------------------------------------------------unused

    # url(r'^(?P<pk>[0-9]+)/phone/$', views.DeletePhone.as_view(
    #     template_name='user/user_confirm_delete.html'), name='delete_phone'),
    # url(r'^(?P<pk>[0-9]+)/email$', views.DeleteEmail.as_view(
    #     template_name='user/user_confirm_delete.html'), name='delete_email'),
    # url(r'^(?P<pk>[0-9]+)/address$', views.DeleteAddress.as_view(
    #     template_name='user/user_confirm_delete.html'), name='delete_address'),

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
