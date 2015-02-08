from django.shortcuts import render_to_response
from django.template import RequestContext
from app.models import *

# Create your views here.


def index(request):
    imgs = image.objects.filter(pro_id = -1)
    return render_to_response('index.html', {'imgs':imgs, 'request': request}, context_instance=RequestContext(request))


def index_inv(request):
    imgs = image.objects.filter(pro_id = -1)
    return render_to_response('index_inv.html', {'imgs':imgs, 'request': request}, context_instance=RequestContext(request))


def financing(request):
	field = request.GET['field']
	province = request.GET['province']
	type = request.GET['type']
	stage = request.GET['stage']
	recommand = request.GET['recommand']
	projects = project.objects.filter(is_roadshowing = '当期路演')
	raw_sql = "SELECT DISTINCT province FROM project WHERE is_roadshowing = '当期路演'"
	provinces = project.objects.raw(raw_sql)
	return render_to_response('base_financing.html', {
		'projects':projects, 
		'field':field,
		'province':province,
		'type':type,
		'stage':stage,
		'request': request
	}, context_instance=RequestContext(request))


def policy(request):
    return render_to_response('policy.html', {'request': request}, context_instance=RequestContext(request))


def community(request):
    return render_to_response('community.html', {'request': request}, context_instance=RequestContext(request))


def about(request):
    return render_to_response('about.html', {'request': request}, context_instance=RequestContext(request))


def contract(request):
    return render_to_response('contract.html', {'request': request}, context_instance=RequestContext(request))


def feedback(request):
    return render_to_response('feedback.html', {'request': request}, context_instance=RequestContext(request))
