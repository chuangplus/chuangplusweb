from django.shortcuts import render_to_response

from app.models import *


# Create your views here.

def index(request):
	user = request.user;
	imgs = image.objects.filter(pro_id = -1)
	return render_to_response('index.html',{'imgs':imgs, 'user':user})

def index_inv(request):
	user = request.user;
	imgs = image.objects.filter(pro_id = -1)
	return render_to_response('index_inv.html',{'imgs':imgs, 'user':user})

def financing(request):
    user = request.user;
    return render_to_response('base_financing.html', {'user':user})
	
def policy(request):
    user = request.user;
    return render_to_response('policy.html', {'user':user})
	
def community(request):
    user = request.user;
    return render_to_response('community.html', {'user':user})
	
def about(request):
    user = request.user;
    return render_to_response('about.html', {'user':user})

def contract(request):
    user = request.user;
    return render_to_response('contract.html', {'user':user})

def feedback(request):
    user = request.user;
    return render_to_response('feedback.html', {'user':user})
