from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [ 
	url(r'^$', views.recipe_list, name='recipe_list'),
	url(r'^recipe/(?P<pk>\d+)/$', views.recipe_detail, name='recipe_detail'),
	url(r'^recipe/new/$', views.recipe_new, name='recipe_new'),
	url(r'^recipe/(?P<pk>\d+)/edit/$', views.recipe_edit, name='recipe_edit'),
	url(r'^login/$', auth_views.login, name='login_user'),
	url(r'^recipe/search/$', views.search, name='search'),
	url(r'^logout/$', views.logout_view, name='logout_user')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
