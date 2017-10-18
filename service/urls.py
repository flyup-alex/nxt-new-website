from django.conf.urls import url
from . import views

urlpatterns = [

    #service/
    url(r'^$', views.index, name='index'),

    #service/single-service/
    url(r'^(?P<title_seo>[a-zA-Z][\w-]{1,90})/', views.single_service, name='single_service')




]


