from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from .views import guest_register_page,RegisterView,LoginView

urlpatterns = [
    url(r'^login/$',LoginView.as_view(),name='login'),
    url(r'^logout/$',LogoutView.as_view(),name='logout'),
    url(r'^register/$',RegisterView.as_view(),name='register'),
    url(r'^guest/$',guest_register_page,name='guest'),

]