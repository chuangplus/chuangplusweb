# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext

def user_login(request):
<<<<<<< HEAD
	if request.user.is_authenticated():  
		return  HttpResponse('你已经登录')  
	if request.method == 'POST':  
		user = authenticate(username=request.POST['username'], password=request.POST['password']) 
		if user is not None:  
			if user.is_active:  
				login(request, user)   
				print request.user 
				return HttpResponseRedirect('/') 
			else:  
				return HttpResponse('用户没有启用!')  
		else:  
			return HttpResponse('用户名或者密码错误！')  
	else:  
		return render_to_response('login.html', context_instance=RequestContext(request))  

def user_logout(request):
	logout(request)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
	
def cyz_register(request):
	if request.method == 'POST':  
		form = UserRegisterForm(data=request.POST)  
		if form.is_valid():  
			new_user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])  
			new_user.save()  
			return render(request,'index.html')  
		else:  
			return render(request,'register.html', {'form':form})  
			#超链接点击过来的注册  
	else:  
		return render(request,'register.html')
=======
    if request.user.is_authenticated():
        return  HttpResponse('你已经登录')
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                print(request.user)
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
>>>>>>> dev-python3
