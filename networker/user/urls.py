""" user app URL Configuration """

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [

    # ----------------------------------------------------------------listview
    url(r'^$', login_required(views.ListingUser.as_view(template_name='user/user_list.html')), name='listing_user'),
    url(r'^(?P<pk>[0-9]+)/phone$', login_required(views.ListingPhone.as_view(template_name='user/userphone_list.html')), name='listing_phone'),
    url(r'^(?P<pk>[0-9]+)/email$', login_required(views.ListingEmail.as_view(template_name='user/useremail_list.html')), name='listing_email'),
    url(r'^(?P<pk>[0-9]+)/address$', login_required(views.ListingAddress.as_view(template_name='user/useraddress_list.html')), name='listing_address'),
    url(r'^(?P<pk>[0-9]+)/socialmedia$', login_required(views.ListingSocialMedia.as_view(template_name='user/usersocialmedia_list.html')), name='listing_social_media'),
    url(r'^(?P<pk>[0-9]+)/job$', login_required(views.ListingJob.as_view(template_name='user/userjob_list.html')), name='listing_job'),
    url(r'^(?P<pk>[0-9]+)/education$', login_required(views.ListingEducation.as_view(template_name='user/usereducation_list.html')), name='listing_education'),
    url(r'^(?P<pk>[0-9]+)/skill$', login_required(views.ListingSkill.as_view(template_name='user/userskill_list.html')), name='listing_skill'),


    # --------------------------------------------------------------updateview
    url(r'^(?P<pk>[0-9]+)/main$', login_required(views.UserUpdateMain.as_view(
        template_name='user/create_update_form.html')), name='update_main'),
    url(r'^(?P<pk>[0-9]+)/additional$',
        login_required(views.UserUpdateAdditional.as_view(template_name='user/create_update_form.html')), name='update_additional'),
    url(r'^(?P<pk>[0-9]+)/image$', login_required(views.UserUpdateImage.as_view(
        template_name='user/create_update_form.html')), name='update_image'),
    # url(r'^(?P<pk>[0-9]+)/membership$', login_required(views.UserUpdateMembership.as_view(
        # template_name='user/create_update_form.html')), name='update_membership'),


    # ------------------------------------------------------------user profile
    url(r'^(?P<pk>[0-9]+)/$', views.UserProfile, name='user_profile'),
    

    # --------------------------------------------------updateview by category
    url(r'^(?P<pk>[0-9]+)/phone/(?P<phone>[0-9]+)$', login_required(views.UserUpdatePhone.as_view(
        template_name='user/create_update_form.html')), name='update_phone'),
    url(r'^(?P<pk>[0-9]+)/email/(?P<email>[0-9]+)$', login_required(views.UserUpdateEmail.as_view(
        template_name='user/create_update_form.html')), name='update_email'),
    url(r'^(?P<pk>[0-9]+)/address/(?P<address>[0-9]+)$', login_required(views.UserUpdateAddress.as_view(
        template_name='user/create_update_form.html')), name='update_address'),
    url(r'^(?P<pk>[0-9]+)/social_media/(?P<social_media>[0-9]+)$', login_required(views.UserUpdateSocialMedia.as_view(
        template_name='user/create_update_form.html')), name='update_social_media'),
    url(r'^(?P<pk>[0-9]+)/job/(?P<job>[0-9]+)$', login_required(views.UserUpdateJob.as_view(
        template_name='user/create_update_form.html')), name='update_job'),
    url(r'^(?P<pk>[0-9]+)/education/(?P<education>[0-9]+)$', login_required(views.UserUpdateEducation.as_view(
        template_name='user/create_update_form.html')), name='update_education'),
    url(r'^(?P<pk>[0-9]+)/skill/(?P<skill>[0-9]+)$', login_required(views.UserUpdateSkill.as_view(
        template_name='user/create_update_form.html')), name='update_skill'),


    # --------------------------------------------------------------createview
    url(r'^(?P<pk>[0-9]+)/phone/create$', login_required(views.CreatePhone.as_view(
        template_name='user/create_update_form.html')), name='create_phone'),
    url(r'^(?P<pk>[0-9]+)/email/create$', login_required(views.CreateEmail.as_view(
        template_name='user/create_update_form.html')), name='create_email'),
    url(r'^(?P<pk>[0-9]+)/address/create$', login_required(views.CreateAddress.as_view(
        template_name='user/create_update_form.html')), name='create_address'),
    url(r'^(?P<pk>[0-9]+)/social_media/create$', login_required(views.CreateSocialMedia.as_view(
        template_name='user/create_update_form.html')), name='create_social_media'),
    url(r'^(?P<pk>[0-9]+)/job/create$', login_required(views.CreateJob.as_view(
        template_name='user/create_update_form.html')), name='create_job'),
    url(r'^(?P<pk>[0-9]+)/education/create$', login_required(views.CreateEducation.as_view(
        template_name='user/create_update_form.html')), name='create_education'),
    url(r'^(?P<pk>[0-9]+)/skill/create$', login_required(views.CreateSkill.as_view(
        template_name='user/create_update_form.html')), name='create_skill'),


    # ------------------------------------------------------------------unused
    # url(r'^(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='detail'),
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
