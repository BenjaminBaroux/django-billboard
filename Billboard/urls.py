from django.conf.urls import url


from Billboard import views
from django.contrib import admin

urlpatterns =[
    url(r'^$',views.index, name='index'),
    url(r'^newpost$', views.newpost, name='newpost'),
]