from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from django.http import Http404
from .models import Product

# Create your views here.
class ProductListView(ListView):
	def get_queryset(self,*args,**kwargs):
		request=self.request
		return Product.objects.all()
class ProductDetaiSlugView(DetailView):
	def get_queryset(self,*args,**kwargs):
		request=self.request
		return Product.objects.all()