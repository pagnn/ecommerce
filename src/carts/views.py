from django.shortcuts import render,redirect
from accounts.models import GuestEmail

from addresses.forms import AddressForm
from addresses.models import Address
from accounts.forms import LoginForm,GuestForm
from products.models import Product
from .models import Cart
from orders.models import Order
from billing.models import BillingProfile
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

	login_form=LoginForm()
	guest_form=GuestForm()
	address_form=AddressForm()
	shipping_address_id=request.session.get('shipping_address_id',None)
	billing_address_id=request.session.get('billing_address_id',None)

	billing_profile,billing_profile_created=BillingProfile.objects.new_or_get(request)
	address_qs=None
	if billing_profile is not None:
		if request.user.is_authenticated():
			address_qs=Address.objects.filter(billing_profile=billing_profile)
		order_obj,order_obj_created=Order.objects.new_or_get(billing_profile,cart_obj)	
		if shipping_address_id:
			shipping_address=Address.objects.get(id=shipping_address_id)
			order_obj.shipping_address=shipping_address
			del request.session['shipping_address_id']
		if billing_address_id:
			billing_address=Address.objects.get(id=billing_address_id)
			order_obj.billing_address=billing_address
			del request.session['billing_address_id']
		if shipping_address_id or billing_address_id:
			order_obj.save()
	if request.method == 'POST':
		is_done=order_obj.check_done()
		if is_done:
			order_obj.mark_paid()
			request.session['cart_items']=0
			del request.session['cart_id']
		return redirect('carts:success')
	context={
		'object':order_obj,
		'billing_profile':billing_profile,
		'login_form':login_form,
		'guest_form':guest_form,
		'address_form':address_form,
		'address_qs':address_qs,
	}
	return render(request,'carts/checkout.html',context)


def checkout_done_view(request):
	context={}
	return render(request,'carts/checkout_done.html',context)