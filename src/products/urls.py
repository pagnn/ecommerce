from django.conf.urls import url
from .views import ProductDetaiSlugView,ProductListView

urlpatterns = [
    url(r'^$', ProductListView.as_view(),name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetaiSlugView.as_view(),name='detail'),

]