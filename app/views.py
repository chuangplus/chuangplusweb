from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import Context

# Create your views here.

def index(request):
    return render_to_response('index.html')

def financing(request):
    return render_to_response('base_financing.html')