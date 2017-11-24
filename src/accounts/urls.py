from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from .views import login_page,register_page,guest_register_page

urlpatterns = [
    url(r'^login/$',login_page,name='login'),
    url(r'^logout/$',LogoutView.as_view(),name='logout'),
    url(r'^register/$',register_page,name='register'),
    url(r'^guest/$',guest_register_page,name='guest'),

]