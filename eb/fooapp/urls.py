# fooapp/urls.py (newly created)

from django.conf.urls import url
from fooapp import views

urlpatterns = [
   url('^$', views.index, name='index'),
   url('^template/', views.template, name='template'),
]
