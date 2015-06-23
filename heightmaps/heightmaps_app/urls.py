from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^export/', views.exportMap, name='exportMap'),
    url(r'^$', views.index, name='index'),

]