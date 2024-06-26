from django.contrib import admin
from django.urls import path, include
from ribble import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.form, name='Form'),
    path('Home', views.home, name='Home'),
    path('About', views.about, name='About'),
    path('log', views.log, name='log'),
    path('Home/<id>/', views.home, name='log'),
    path('About/<id>/', views.about, name='dif'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()