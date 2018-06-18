from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^invite', views.invite, name='invite'),
    url(r'^check', views.check, name='check'),
    url(r'^asdf', views.check2, name='check2'),
    url(r'^process', views.register_invite_ticket, name='register_invite_ticket'),
]
