""" networker app URL Configuration """


from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'user.views.index', name='index'),
    url(r'^register/$', 'user.views.register', name='register'),
    url(r'^login/$', 'user.views.user_login', name='login'),
    url(r'^restricted/$', 'user.views.restricted', name='restricted'),
    url(r'^logout/$', 'user.views.user_logout', name='logout'),
    url(r'^groups/$', include('group.urls')),
    url(r'^users/', include('user.urls')),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


