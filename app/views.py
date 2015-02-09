from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import Context
from models import *

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
    projects_past = project.objects.all();
    return render_to_response('project_financing.html', {'user':user, 'projects_past':projects_past})

def library(request):
    user = request.user;
    projects_past = project.objects.all();
    return render_to_response('project_library.html', {'user':user, 'projects_past':projects_past})

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
