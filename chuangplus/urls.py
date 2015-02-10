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

    # login
    url(r'^login/$', 'app.user.user_login'),
    # logout
    url(r'^logout/$', 'app.user.user_logout'),
    # register
    url(r'^register/$', 'app.user.cyz_register'),

    # financing
<<<<<<< HEAD
    url(r'^financing/$', financing, name="financing"),
=======
    url(r'^financing/$', financing),
>>>>>>> 88ea873062e119393e293704238e75f1f92fc760
    # library
    url(r'^library/$', library),
    # policy
    url(r'^policy/$', policy),
    # community
    url(r'^community/$', community, name="community"),
    # about
    url(r'^about/$', about, name="about"),
    # contract
    url(r'^contract/$', contract, name="contract"),
    # feedback
    url(r'^feedback/$', feedback, name="feedback"),
    # feedback
    url(r'^redirect_back/$', redirect_back, name="redirect_back"),

    # account
    url(r"^account/login/$", LoginView.as_view(), name="account_login"),
    url(r"^account/signup/$", SignupView.as_view(), name="account_signup"),
    url(r"^account/signup/finish$", signup_finish, name="account_signup_finish"),
    url(r"^account/signup_inv/$", SignupInvView.as_view(), name="account_signup_inv"),
    url(r"^account/signup_inv_precheck/$", SignupInvPrecheckView.as_view(), name="account_signup_inv_precheck"),
    url(r"^account/signup_inv/finish$", signup_inv_finish, name="account_signup_inv_finish"),
    url(r"^account/", include("account.urls")),

    # captcha
    url(r'^captcha/', include('captcha.urls')),

    # index-investor
    url(r'^inv/$', 'app.views.index_inv', name="index_inv"),
    # index
    url(r'^$', 'app.views.index', name='home'),

)
