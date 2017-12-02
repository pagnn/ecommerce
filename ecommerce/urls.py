"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView,RedirectView
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from accounts.views import GuestRegisterView,LoginView,RegisterView


from .views import home_page,about_page,contact_page
from addresses.views import AddressCreateView,AddressUpdateView,AddressListView,checkout_address_create_view,checkout_address_reuse_view
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$',LoginView.as_view(),name='login'),
    url(r'^logout/$',LogoutView.as_view(),name='logout'),
    url(r'^register/$',RegisterView.as_view(),name='register'),
    url(r'^guest/$',GuestRegisterView.as_view(),name='guest'),
    url(r'^contact/$', contact_page,name='contact'),
    url(r'^about/$', about_page,name='about'),
    url(r'^addresses/$',AddressListView.as_view(),name='addresses'),
    url(r'^addresses/create/$',AddressCreateView.as_view(),name='address-create'),   
    url(r'^addresses/(?P<pk>\d+)/$',AddressUpdateView.as_view(),name='address-update'),
    url(r'^address/$',RedirectView.as_view(url='/addresses')),
    url(r'^checkout/address/create/$',checkout_address_create_view,name='address_create'),
    url(r'^checkout/address/reuse/$',checkout_address_reuse_view,name='address_reuse'),
    url(r'^$', home_page,name='home'),
    url(r'^products/',include('products.urls',namespace='products')),
    url(r'^search/',include('search.urls',namespace='search')),
    url(r'^carts/',include('carts.urls',namespace='carts')),
    url(r'^account/',include('accounts.urls',namespace='accounts')),
    url(r'^accounts/',include('accounts.passwords.urls')),
    url(r'^accounts/$',RedirectView.as_view(url='/account')),
    url(r'^billing/',include('billing.urls',namespace='billing')),
    url(r'^marketing/',include('marketing.urls',namespace='marketing')),
    url(r'^orders/',include('orders.urls',namespace='orders')),
]
if settings.DEBUG:
    urlpatterns=urlpatterns+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)