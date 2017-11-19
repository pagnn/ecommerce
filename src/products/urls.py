from django.conf.urls import url
from .views import ProductDetaiSlugView,ProductListView

urlpatterns = [
    url(r'^$', ProductListView.as_view(),name='product_list'),
    url(r'(?P<slug>[\w_]+)/$', ProductDetaiSlugView.as_view(),name='product_detail'),

]