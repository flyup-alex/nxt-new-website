from django.conf.urls import url
from . import views

urlpatterns = [

    #szkolenia/
    url(r'^$', views.index, name='index'),

    #/szkolenia/perfect-seller
    url(r'^(?P<training_title>[a-zA-Z][\w-]{1,90})/', views.show, name='show'),

]


