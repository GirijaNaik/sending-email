from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #url(r'^home/$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^account_activate_sent/$', views.signup, name='account_activate_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
