from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from django.http import Http404

from carts.models import Cart
from .models import Product

# Create your views here.
class ProductListView(ListView):
	def get_queryset(self,*args,**kwargs):
		request=self.request
		return Product.objects.all()
class ProductDetaiSlugView(DetailView):
	def get_context_data(self,*args,**kwargs):
		context=super(ProductDetaiSlugView,self).get_context_data(*args,**kwargs)
		cart_obj,new_obj=Cart.objects.new_or_get(self.request)
		context['cart']=cart_obj
		return context
	def get_queryset(self,*args,**kwargs):
		request=self.request
		return Product.objects.all()