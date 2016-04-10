"""Define URL patterns for web_forums."""

from django.conf.urls import url

from. import views

urlpatterns = [
	# Home page
	url(r'^$', views.index, name='index'),

	#Show the topics
	url(r'^topics/$', views.topics, name = 'topics'),	

	#Detailed page of single topic
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name = 'topic'),	
]