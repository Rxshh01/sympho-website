from django.urls import path,include
from . import views

from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.main_view1,name="main_view1"),
    path('paper/', views.home, name="home"),
    path('accounts/', include('allauth.urls')),
    path('paper/submission', views.submission, name="submission"),
    path('paper/submitted', views.submitted, name="submitted"),
    path('new', views.new, name="new"),
    path('academic_writing',views.academic_home,name="academic_writing"),
    path('noniitb_register',views.noniitb_view,name="non_iitb_url"),
     path('iitb_register',views.iitb_view,name="iitb_url"),
#    path('poster_url', views.poster_view, name="poster_name"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
