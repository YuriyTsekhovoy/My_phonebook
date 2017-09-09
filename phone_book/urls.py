from django.conf.urls import url
from . import views

#app_name = "phone_book"
urlpatterns = [
    url(r'^$', views.sign_list, name='sign_list'),
    url(r'^sign/(?P<pk>[0-9]+)/$', views.sign_detail, name='sign_detail'),
    url(r'^sign/new/$', views.sign_new, name='sign_new'),
    url(r'^sign/(?P<pk>[0-9]+)/edit/$', views.sign_edit, name='sign_edit'),
    url(r'^sign/(?P<pk>[0-9]+)/delete/$', views.sign_delete, name='sign_delete'),
    url(r'^sign/(?P<pk>[0-9]+)/copy/$', views.sign_copy, name='sign_copy'),
]
