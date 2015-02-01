from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from app.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chuangplus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # financing
    url(r'^financing/$', financing),
    # policy
    url(r'^policy/$', policy),
    # community
    url(r'^community/$', community),
	
	# index
    url(r'^$', 'app.views.index'),
	
)
