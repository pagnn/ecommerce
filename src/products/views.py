from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from django.http import Http404


from analytics.mixins import ObjectViewedMixin
from carts.models import Cart
from .models import Product

# Create your views here.
class ProductListView(ListView):
	def get_queryset(self,*args,**kwargs):
		request=self.request
		return Product.objects.all()
	def get_context_data(self,*args,**kwargs):
		context=super(ProductListView,self).get_context_data(*args,**kwargs)
		cart_obj,new_obj=Cart.objects.new_or_get(self.request)
		context['cart']=cart_obj
		return context	
class ProductDetaiSlugView(ObjectViewedMixin,DetailView):
	def get_context_data(self,*args,**kwargs):
		context=super(ProductDetaiSlugView,self).get_context_data(*args,**kwargs)
		cart_obj,new_obj=Cart.objects.new_or_get(self.request)
		context['cart']=cart_obj
		print (context)
		return context
	def get_queryset(self,*args,**kwargs):
		request=self.request
		return Product.objects.all()

	def get_object(self,*args,**kwargs):
		request=self.request

		slug=self.kwargs.get('slug')

		try:
			instance=Product.objects.get(slug=slug,active=True)
		except Product.DoesNotExist:
			raise Http404('Not Found....')
		except Product.MultipleObjectsReturned:
			qs=Product.objects.filter(slug=slug,active=True)
			instance=qs.first()
		except:
			raise Http404('Uhhmmm...')
		return instance
