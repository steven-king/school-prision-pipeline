from django.conf.urls import patterns, include, url
from county_info import views

urlpatterns = patterns('county_info.views',
	url(r'^$', views.home, name='map_home'),
	url(r'^mobile/$', views.mobile, name='mobile_home'),
	url(r'^api/graduation_rates$', 'graduation_rates'),
)
