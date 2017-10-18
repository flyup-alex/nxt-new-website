"""nxt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from . import settings
from .settings import STATIC_ROOT, STATIC_URL
from site_settings.views import index
from django.conf.urls import url, include
from about.views import contact


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^portfolio/', include('portfolio.urls', namespace='portfolio')),
    url(r'^o-nas/', include('about.urls', namespace='about')),
    url(r'^kontakt/$', contact, name='contact'),
    url(r'^uslugi/', include('service.urls', namespace='service')),
    url(r'^szkolenia/', include('training.urls', namespace='training')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),


] + static(STATIC_URL, document_root=STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
