from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import include
from django.contrib import admin

urlpatterns = [ 
	url(r'^$', views.recipe_list, name='recipe_list'),
	url(r'^recipe/(?P<pk>\d+)/$', views.recipe_detail, name='recipe_detail'),
	url(r'^recipe/new/$', views.recipe_new, name='recipe_new'),
	url(r'^recipe/(?P<pk>\d+)/edit/$', views.recipe_edit, name='recipe_edit'),
	url(r'accounts/', include('django.contrib.auth.urls')),
	url(r'^accounts/login/$', views.loginView, name='home'),
	url(r'^recipe/search/$', views.search, name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
