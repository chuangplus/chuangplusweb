from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from app.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chuangplus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # financing
    url(r'^financing/$', financing),
	# index
    url(r'^.*$', 'app.views.index'),
	
)
