from django.conf.urls import patterns, include, url
from county_info import views

urlpatterns = patterns('county_info.views',
	url(r'^$', views.home, name='map_home'),
	url(r'^mobile/$', views.mobile, name='mobile_home'),
	url(r'^api/graduation_rates$', 'graduation_rates'),
	url(r'^api/sat_scores$', 'sat_scores'),
	url(r'^api/freelunch_rates$', 'freelunch_rates'),
	url(r'^api/discipline_rates$', 'discipline_rates'),
	url(r'^api/expenses$', 'expenses'),
	url(r'^api/districts/(?P<pk>[0-9]+)/$', 'district_detail'),
)
