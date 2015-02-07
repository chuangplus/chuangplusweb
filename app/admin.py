# coding: utf-8
from django.contrib import admin

# Register your models here.

from app.models import *

admin.site.register( userinfo )
admin.site.register( project )
admin.site.register( member )
admin.site.register( post )
admin.site.register( relation )
admin.site.register( image )
	