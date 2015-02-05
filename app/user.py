# -*- coding: utf-8 -*- 
from models import *
from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.template import RequestContext
import sys


def user_login(request):
	if request.user.is_authenticated():  
		return  HttpResponse('你已经登录')  
	if request.method == 'POST':  
		user = authenticate(username=request.POST['username'], password=request.POST['password']) 
		if user is not None:  
			if user.is_active:  
				login(request, user)   
				print request.user 
				return render_to_response('index.html', context_instance=RequestContext(request))  
			else:  
				return HttpResponse('用户没有启用!')  
		else:  
			return HttpResponse('用户名或者密码错误！')  
	else:  
		return render_to_response('login.html', context_instance=RequestContext(request))  

def user_logout(request):
	logout(request)
	return render_to_response('index.html', context_instance=RequestContext(request))