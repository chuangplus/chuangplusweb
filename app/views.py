from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic.edit import FormView
from app.models import *
import app.forms
import account.forms
import account.models
import account.views
from account.utils import default_redirect
from account.decorators import login_required


# Create your views here.


def index(request):
    imgs = image.objects.filter(pro_id = -1)
    return render_to_response('index.html', {'imgs':imgs, 'request': request}, context_instance=RequestContext(request))


def index_inv(request):
    imgs = image.objects.filter(pro_id = -1)
    return render_to_response('index_inv.html', {'imgs':imgs, 'request': request}, context_instance=RequestContext(request))


def financing(request):
<<<<<<< HEAD
    user = request.user;
    projects_past = project.objects.all();
    return render_to_response('base_financing.html', {'user':user, 'projects_past':projects_past})
	
=======
    field = request.GET.get('field', '')
    province = request.GET.get('province', '')
    type = request.GET.get('type', '')
    stage = request.GET.get('stage', '')
    recommand = request.GET.get('recommand', '')
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


>>>>>>> dev-python3
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


def redirect_back(request):
    redirect_url = request.session.get('referer', None)
    if redirect_url is None:
        redirect_url = '/'
    else:
        del request.session['referer']
    return redirect(redirect_url)


@login_required
def signup_finish(request):
    return render_to_response('signup_finish.html', {'request': request}, context_instance=RequestContext(request))


@login_required
def signup_inv_finish(request):
    return render_to_response('signup_inv_finish.html', {'request': request}, context_instance=RequestContext(request))


class LoginView(account.views.LoginView):

    form_class = account.forms.LoginEmailForm


class SignupView(account.views.SignupView):

    form_class = app.forms.SignupForm
    identifier_field = "email"

    def generate_username(self, form):
        # do something to generate a unique username (required by the
        # Django User model, unfortunately)
        username = form.cleaned_data["email"]
        return username

    def after_signup(self, form):
        self.create_profile(form)
        super(SignupView, self).after_signup(form)

    def create_profile(self, form):
        ui = userinfo(user=self.created_user)
        ui.name = form.cleaned_data["name"]
        ui.save()

    def dispatch(self, request, *args, **kwargs):
        if request.session.get('referer', None) is None:
            self.request.session['referer'] = request.META.get('HTTP_REFERER', '/')
        return super(SignupView, self).dispatch(request, *args, **kwargs)


class SignupInvView(account.views.SignupView):

    form_class = app.forms.SignupInvForm
    identifier_field = "email"
    ACCOUNT_SIGNIN_INV_PRECHECK_URL = "/account/signup_inv_precheck/"

    def generate_username(self, form):
        # do something to generate a unique username (required by the
        # Django User model, unfortunately)
        username = form.cleaned_data["email"]
        return username

    def after_signup(self, form):
        self.create_profile(form)
        super(SignupInvView, self).after_signup(form)

    def create_profile(self, form):
        ui = userinfo(user=self.created_user)
        ui.name = form.cleaned_data["name"]
        ui.phone = form.cleaned_data["phone"]
        ui.save()

    def dispatch(self, request, *args, **kwargs):
        invite_code = request.session.get('invite_code', None)
        if invite_code is None:
            if request.session.get('referer', None) is None:
                self.request.session['referer'] = request.META.get('HTTP_REFERER', '/')
            return redirect(self.ACCOUNT_SIGNIN_INV_PRECHECK_URL)
        else:
            del self.request.session['invite_code']
            return super(SignupInvView, self).dispatch(request, *args, **kwargs)


class SignupInvPrecheckView(FormView):

    template_name = "signup_inv_precheck.html"
    template_name_ajax = "ajax/signup_inv_precheck.html"
    form_class = app.forms.SignupInvPrecheckForm
    form_kwargs = {}
    redirect_field_name = "next"
    ACCOUNT_SIGNIN_INV_PRECHECK_REDIRECT_URL = "/account/signup_inv/"

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect(self.get_success_url())
        return super(SignupInvPrecheckView, self).get(*args, **kwargs)

    def get_template_names(self):
        if self.request.is_ajax():
            return [self.template_name_ajax]
        else:
            return [self.template_name]

    def get_context_data(self, **kwargs):
        ctx = kwargs
        redirect_field_name = self.get_redirect_field_name()
        ctx.update({
            "redirect_field_name": redirect_field_name,
            "redirect_field_value": self.request.REQUEST.get(redirect_field_name, ""),
        })
        return ctx

    def get_form_kwargs(self):
        kwargs = super(SignupInvPrecheckView, self).get_form_kwargs()
        kwargs.update(self.form_kwargs)
        return kwargs

    def form_valid(self, form):
        self.request.session['invite_code'] = form.cleaned_data['invite_code']
        return redirect(self.get_success_url())

    def get_success_url(self, fallback_url=None, **kwargs):
        if fallback_url is None:
            fallback_url = self.ACCOUNT_SIGNIN_INV_PRECHECK_REDIRECT_URL
        kwargs.setdefault("redirect_field_name", self.get_redirect_field_name())
        return default_redirect(self.request, fallback_url, **kwargs)

    def get_redirect_field_name(self):
        return self.redirect_field_name

    def dispatch(self, request, *args, **kwargs):
        if request.session.get('referer', None) is None:
           self.request.session['referer'] = request.META.get('HTTP_REFERER', '/')
        return super(SignupInvPrecheckView, self).dispatch(request, *args, **kwargs)
