from django.urls import path,include
from . import views

# from django.views.generic import TemplateView
# from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('poster/', views.poster_view, name="poster_url"),
    path('poster/poster_submit', views.poster_submit, name="poster_submit"),
    path('accounts/', include('allauth.urls')),
    # path('paper/submission', views.submission, name="submission"),
    # path('paper/submitted', views.submitted, name="submitted"),
    # path('poster_url', views.poster_view, name="poster_name"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
