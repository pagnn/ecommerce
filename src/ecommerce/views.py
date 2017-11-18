from django.contrib.auth import authenticate,login,get_user_model
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import ContactForm,LoginForm,RegisterForm
def home_page(request):
	context={
		'title':'Home',
		'premium':'Yeahhhhhhh...'
	}
	return render(request,'home.html',context)
def about_page(request):
	context={
		'title':'About'
	}	
	return render(request,'about.html',context)
def contact_page(request):
	contact_form=ContactForm( request.POST or None)
	context={
		'title':'Contact',
		'form':contact_form,
	}
	if contact_form.is_valid():
		cd=contact_form.cleaned_data
		print (cd)
	return render(request,'contact.html',context)
def login_page(request):
	login_form=LoginForm( request.POST or None)
	context={
		'form':login_form,
	}
	if login_form.is_valid():
		cd=login_form.cleaned_data
		username=cd['username']
		password=cd['password']
		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('/')
		else:
			print ('error')
	return render(request,'auth/login.html',context)
User=get_user_model()
def register_page(request):
	register_form=RegisterForm( request.POST or None)
	context={
		'form':register_form,
	}
	if register_form.is_valid():
		cd=register_form.cleaned_data
		username=cd.get('username')
		password=cd.get('password')
		email=cd.get('email')
		new_user=User.objects.create_user(username,email,password)
		print (new_user)
		print (cd)
		print('Register...')	
	return render(request,'auth/register.html',context)