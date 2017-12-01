from django.contrib.auth import authenticate,login,get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url
from django.utils.safestring import mark_safe
from django.views.generic.edit import FormMixin
from django.views.generic import CreateView,FormView,DetailView,View
from django.contrib import messages
from django.core.urlresolvers import reverse
from .forms import LoginForm,RegisterForm,GuestForm,ReactiveEmailForm
from .models import GuestEmail,EmailActivation
from .signals import user_logged_in_signal

	
class AccountHomeView(LoginRequiredMixin,DetailView):
	template_name='accounts/home.html'
	def get_object(self):
		return self.request.user

def guest_register_page(request):
	form=GuestForm(request.POST or None)
	context={
		'form':form,
	}
	next_=request.GET.get('next')
	next_post=request.POST.get('next')
	redirect_path=next_ or next_post or None
	if form.is_valid():
		email=form.cleaned_data.get('email')
		new_guest_email=GuestEmail.objects.create(email=email)
		request.session['guest_email_id']=new_guest_email.id
		if is_safe_url(redirect_path,request.get_host()):
			return redirect(redirect_path)
		else:
			return redirect('register')
	return redirect('register')
class LoginView(FormView):
	form_class=LoginForm
	template_name='accounts/login.html'
	def form_valid(self,form):
		request=self.request
		next_=request.GET.get('next')
		next_post=request.POST.get('next')
		redirect_path=next_ or next_post or None

		cd=form.cleaned_data
		email=cd['email']
		password=cd['password']
		user=authenticate(request,email=email,password=password)
		if user is not None:
			if not user.is_active:
				messages.error(request,'This user is not active.')
				return super(LoginView,self).form_invalid(form)
			login(request,user)
			user_logged_in_signal.send(user.__class__,instance=user,request=request)
			try:
				del request.session['guest_email_id']
			except:
				pass
			if is_safe_url(redirect_path,request.get_host()):
				return redirect(redirect_path)
			else:
				return redirect('/')
		return super(LoginView,self).form_invalid(form)

User=get_user_model()

class EmailActivationView(FormMixin,View):
	success_url='/login/'
	form_class=ReactiveEmailForm
	key=None
	def get_context_data(self,*args,**kwargs):
		context = super(EmailActivationView,self).get_context_data(*args,**kwargs)
		context['form'] = self.get_form()
		return context	
	def get(self,request,key=None,*args,**kwargs):
		self.key=key
		if key is not None:
			qs=EmailActivation.objects.filter(key__iexact=key)
			confirmed_qs=qs.confirmable()
			if confirmed_qs.count() == 1:
				obj=confirmed_qs.first()
				obj.activate()
				msg="Your activation email has been confirmed.Please Login."
				messages.success(request,mark_safe(msg))
				return redirect("/login/")
			else:
				activated_qs=qs.filter(activated=True)
				if activated_qs.exists():
					reset_link=reverse("password_reset")
					msg="Your email has already been confirmed.Do you need to <a href='{link}'>reset your password</a>?".format(link=reset_link)
					messages.success(request,mark_safe(msg))
					return redirect('/login/')


		context={
			'form':self.get_form(),
			'key':key,
		}
		return render(request,'registration/emails/activate-error.html',context)
	def post(self,request,*args,**kwargs):
		form=self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self,form):
		msg="Activation sent.Please check your email."
		messages.success(self.request,mark_safe(msg))
		email=form.cleaned_data.get('email')
		obj=EmailActivation.objects.email_exist(email).first()
		user=obj.user
		new_activation=EmailActivation.objects.create(user=user,email=email)
		new_activation.send_activation()
		return super(EmailActivationView,self).form_valid(form)
	def form_invalid(self,form):
		context={
			'form':self.get_form(),
			'key':self.key,
		}
		return render(self.request,'registration/emails/activate-error.html',context)
class RegisterView(CreateView):
	form_class=RegisterForm
	template_name='accounts/register.html'
	success_url="/login/"

