from django.urls import path,include
from . import views

from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView




urlpatterns = [
     path('', views.mtt, name="mtt"),
    path('accounts/', include('allauth.urls')),
    path('mtt_reg', views.mtt_reg, name="mtt_reg"),
    path('accounts/', include('allauth.urls')),
 
 ]

