from django.conf.urls import url
from project import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name='project'

urlpatterns=[
	url(r'^household/$',views.HouseholdList.as_view()),
	url(r'^member/$',views.MemberList.as_view()),
	url(r'^audio/$',views.AudioList.as_view()),
	url(r'^photo/$',views.PhotoList.as_view()),
	url(r'^farm/$',views.FarmList.as_view()),
	url(r'^point/$',views.PointList.as_view()),
	url(r'^cropping/$',views.CroppingList.as_view()),
	url(r'^well/$',views.WellList.as_view()),
	url(r'^wellyield/$',views.WellyieldList.as_view()),
	url(r'^household/(?P<pk>[0-9]+)/$',views.HouseholdDetail.as_view()),
	url(r'^member/(?P<pk>[0-9]+)/$',views.MemberDetail.as_view()),
	url(r'^audio/(?P<pk>[0-9]+)/$',views.AudioDetail.as_view()),
	url(r'^photo/(?P<pk>[0-9]+)/$',views.PhotoDetail.as_view()),
	url(r'^farm/(?P<pk>[0-9]+)/$',views.FarmDetail.as_view()),
	url(r'^point/(?P<pk>[0-9]+)/$',views.PointDetail.as_view()),
	url(r'^cropping/(?P<pk>[0-9]+)/$',views.CroppingDetail.as_view()),
	url(r'^well/(?P<pk>[0-9]+)/$',views.WellDetail.as_view()),
	url(r'^wellyield/(?P<pk>[0-9]+)/$',views.WellyieldDetail.as_view()),
	url(r'^$',views.index,name='index'),
	url(r'^read/$',views.read,name='read'),
	url(r'^create/$',views.create,name='create'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^test3/$', views.test3, name='test3'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

