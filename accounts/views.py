from django.contrib.auth import authenticate,login,get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url
from django.views.generic import CreateView,FormView,DetailView,View
from django.contrib import messages
from .forms import LoginForm,RegisterForm,GuestForm
from .models import GuestEmail
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
class RegisterView(CreateView):
	form_class=RegisterForm
	template_name='accounts/register.html'
	success_url="login"

