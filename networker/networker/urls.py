""" networker app URL Configuration """


from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [


    # -----------------------------------------------------------admin + index
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'user.views.index', name='index'),


    # ---------------------------------------------------------------------map
    url(r'^map/$', 'user.views.map', name='map'),


    # ----------------------------------------------------------authentication
    url(r'^register/$', 'user.views.register', name='register'),
    url(r'^login/$', 'user.views.user_login', name='login'),
    url(r'^restricted/$', 'user.views.restricted', name='restricted'),
    url(r'^logout/$', 'user.views.user_logout', name='logout'),


    # -------------------------------------------------------------------group
    url(r'^groups/$', include('group.urls')),


    # --------------------------------------------------------------------user
    url(r'^users/', include('user.urls')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
