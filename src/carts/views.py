from django.shortcuts import render,redirect
from products.models import Product
from .models import Cart
from orders.models import Order
# Create your views here.
def cart_home(request):
	cart_obj,new_obj=Cart.objects.new_or_get(request)
	return render(request,'carts/home.html',{'cart':cart_obj})

def cart_update(request):
	product_id=request.POST.get('product_id')
	if product_id is not None:
		try:
			obj=Product.objects.get(id=product_id)
		except Product.DoesNotExist:
			print('Show message to the user')
			redirect("carts:home")
		cart_obj,new_obj=Cart.objects.new_or_get(request)
		if obj in cart_obj.products.all():
			cart_obj.products.remove(obj)
		else:
			cart_obj.products.add(obj)
	request.session['cart_items']=cart_obj.products.count()
	return redirect("carts:home")

def checkout_home(request):
	cart_obj,new_cart_obj=Cart.objects.new_or_get(request)
	order_obj=None
	if new_cart_obj or cart_obj.products.count() == 0:
		return redirect("carts:home")
	else:
		order_obj,new_order_obj=Order.objects.get_or_create(cart=cart_obj)
	return render(request,'carts/checkout.html',{'object':order_obj})