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
from django.views.generic import TemplateView
from django.conf.urls import url,include
from django.contrib import admin

from .views import home_page,about_page,contact_page
from addresses.views import checkout_address_create_view,checkout_address_reuse_view
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contact/$', contact_page,name='contact'),
    url(r'^about/$', about_page,name='about'),
    url(r'^checkout/address/create/$',checkout_address_create_view,name='address_create'),
    url(r'^checkout/address/reuse/$',checkout_address_reuse_view,name='address_reuse'),
    url(r'^$', home_page,name='home'),
    url(r'^products/',include('products.urls',namespace='products')),
    url(r'^search/',include('search.urls',namespace='search')),
    url(r'^carts/',include('carts.urls',namespace='carts')),
    url(r'^accounts/',include('accounts.urls',namespace='accounts')),
    url(r'^billing/',include('billing.urls',namespace='billing')),
]
if settings.DEBUG:
    urlpatterns=urlpatterns+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)