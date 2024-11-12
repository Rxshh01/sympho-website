from django.urls import path,include
from . import views

from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView




urlpatterns = [
    path('cityplanning/', views.front_page, name="cityplanning"),
    path('accounts/', include('allauth.urls')),
    path('cityplanning/register', views.register_cityplan, name="cityplanning_register"),
    path('cityplanning/registered',views.registered_cityplan,name="cityplanning_registered")
   
]
