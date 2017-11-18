from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()

class ContactForm(forms.Form):
	fullname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
	email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
	content=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Content'}))
	def clean_email(self):
		email=self.cleaned_data.get('email')
		if not 'gmail.com' in email:
			raise forms.ValidationError('Email has to be gmail.')
		return email

class LoginForm(forms.Form):
	username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))

class RegisterForm(forms.Form):
	username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
	email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
	password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))

	def clean_username(self):
		username=self.cleaned_data.get('username')
		qs=User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError('Username is taken.')
		return username
	def clean_email(self):
		email=self.cleaned_data.get('email')
		qs=User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError('Email is taken.')
		return email		

	def clean_password2(self):
		cd=self.cleaned_data
		password=cd['password']
		password2=cd['password2']
		if not password == password2:
			raise forms.ValidationError("Passwords don't match.")
		return password2