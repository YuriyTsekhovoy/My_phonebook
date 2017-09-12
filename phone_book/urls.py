from django.conf.urls import url
from . import views

app_name = "phone_book"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^sign/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^edit$', views.NewSignView.as_view(), name='sign_new'),
    url(r'^sign/(?P<pk>[0-9]+)/edit/$', views.EditNumberView.as_view(), name='edit'),
    url(r'^sign/(?P<pk>[0-9]+)/delete/$', views.DelView.as_view(), name='delete'),
    #url(r'^sign/(?P<pk>[0-9]+)/copy/$', views.sign_copy, name='sign_copy'),
]
