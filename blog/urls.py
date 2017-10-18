from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^(?P<title>[a-zA-Z][\w-]{1,30})/$', views.blog_post, name="blog_post"),
    url(r'^$', views.index, name="blog_index")

]