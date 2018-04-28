from django.conf.urls import url
from . import views

urlpatterns = [ 
	url(r'^$', views.recipe_list, name='recipe_list'),
	url(r'^recipe/(?P<pk>\d+)/$', views.recipe_detail, name='recipe_detail'),
	url(r'^recipe/new/$', views.recipe_new, name='recipe_new'),
	url(r'^recipe/(?P<pk>\d+)/edit/$', views.recipe_edit, name='recipe_edit'),
	url(r'^recipe/search/$', views.search, name='search'),
]