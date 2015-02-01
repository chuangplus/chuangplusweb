from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import Context

# Create your views here.

def index(request):
    return render_to_response('index.html')


def financing(request):
    return render_to_response('base_financing.html')
	
def policy(request):
    return render_to_response('policy.html')
	
def community(request):
    return render_to_response('community.html')
	
def about(request):
    return render_to_response('about.html')

def contract(request):
    return render_to_response('contract.html')

def feedback(request):
    return render_to_response('feedback.html')
