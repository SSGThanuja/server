	# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,reverse

# Create your views here.

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseRedirect,HttpResponse
from .models import Member, Audio, Photo, Household, Farm, Cropping, Point, Well, Wellyield
from .serializers import MemberSerializer, HouseholdSerializer, AudioSerializer, PhotoSerializer, FarmSerializer, PointSerializer, CroppingSerializer, WellSerializer, WellyieldSerializer
from rest_framework import generics
import urllib2
import json 
class HouseholdList(generics.ListCreateAPIView):

		queryset = Household.objects.all()
		#serializer11 = HouseholdSerializer(hold, many=True)
		serializer_class = HouseholdSerializer
		#return Response(serializer11.data)


class MemberList(generics.ListCreateAPIView):

	#def get(self, response):

		queryset = Member.objects.all()
		#serializer_class = MemberSerializer(members, many = True)
		serializer_class=MemberSerializer
		#return Response(serializer.data)


class AudioList(generics.ListCreateAPIView):

	#def get(self, response):

		queryset = Audio.objects.all()
		#serializer_class = AudioSerializer(audios, many=True)
		serializer_class=AudioSerializer
		#return Response(serializer1.data)

class PhotoList(generics.ListCreateAPIView):

	#def get(self, response):

		queryset = Photo.objects.all()
		#serializer2 = PhotoSerializer(photos, many=True)
		serializer_class=PhotoSerializer
		#return Response(serializer2.data)

class FarmList(generics.ListCreateAPIView):

	#def get(self, response):

		queryset = Farm.objects.all()
		#serializer3 = FarmSerializer(farms, many=True)
		serializer_class=FarmSerializer
		#return Response(serializer3.data)

class PointList(generics.ListCreateAPIView):
	#def get(self, response):

		queryset = Point.objects.all()
		#serializer4 = PointSerializer(points, many=True)
		serializer_class=PointSerializer
		#return Response(serializer4.data)

class CroppingList(generics.ListCreateAPIView):

	#def get(self, response):

		queryset = Cropping.objects.all()
		#serializer5 =CroppingSerializer(crops, many=True)
		serializer_class=CroppingSerializer
		#return Response(serializer5.data)

class WellList(generics.ListCreateAPIView):

	#def get(self, response):

		queryset = Well.objects.all()
		#serializer5 =CroppingSerializer(crops, many=True)
		serializer_class=WellSerializer
		#return Response(serializer5.data)

class WellyieldList(generics.ListCreateAPIView):

	#def get(self, response):

		queryset = Wellyield.objects.all()
		#serializer5 =CroppingSerializer(crops, many=True)
		serializer_class=WellyieldSerializer
		#return Response(serializer5.data)


class HouseholdDetail(generics.RetrieveUpdateDestroyAPIView):
		queryset = Household.objects.all()
		#serializer11 = HouseholdSerializer(hold, many=True)
		serializer_class=HouseholdSerializer
		#return Response(serializer11.data)

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):

	#def get(self, response):

		queryset = Member.objects.all()
		#serializer_class = MemberSerializer(members, many = True)
		serializer_class=MemberSerializer
		#return Response(serializer.data)


class AudioDetail(generics.RetrieveUpdateDestroyAPIView):

	#def get(self, response):

		queryset = Audio.objects.all()
		#serializer_class = AudioSerializer(audios, many=True)
		serializer_class=AudioSerializer
		#return Response(serializer1.data)

class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):

	#def get(self, response):

		queryset = Photo.objects.all()
		#serializer2 = PhotoSerializer(photos, many=True)
		serializer_class=PhotoSerializer
		#return Response(serializer2.data)

class FarmDetail(generics.RetrieveUpdateDestroyAPIView):

	#def get(self, response):

		queryset = Farm.objects.all()
		#serializer3 = FarmSerializer(farms, many=True)
		serializer_class=FarmSerializer
		#return Response(serializer3.data)

class PointDetail(generics.RetrieveUpdateDestroyAPIView):
	#def get(self, response):

		queryset = Point.objects.all()
		#serializer4 = PointSerializer(points, many=True)
		serializer_class=PointSerializer
		#return Response(serializer4.data)

class CroppingDetail(generics.RetrieveUpdateDestroyAPIView):

	#def get(self, response):

		queryset = Cropping.objects.all()
		#serializer5 =CroppingSerializer(crops, many=True)
		serializer_class=CroppingSerializer
		#return Response(serializer5.data)

class WellDetail(generics.RetrieveUpdateDestroyAPIView):

	#def get(self, response):

		queryset = Well.objects.all()
		#serializer5 =CroppingSerializer(crops, many=True)
		serializer_class=WellSerializer
		#return Response(serializer5.data)

class WellyieldDetail(generics.RetrieveUpdateDestroyAPIView):

	#def get(self, response):

		queryset = Wellyield.objects.all()
		#serializer5 =CroppingSerializer(crops, many=True)
		serializer_class=WellyieldSerializer
		#return Response(serializer5.data)


def read(request):
	
	req=urllib2.Request("http://127.0.0.1:8000/app/household/")
	opener=urllib2.build_opener()
	f=opener.open(req)
	l=json.loads(f.read())
	k=[]

	return HttpResponse(l)
		
def index(request):
	return render(request,'project/index.html')


def create(request):
	name=request.POST['name']
	gender=request.POST['gender']
	age=request.POST['age']
	obj=Household(name=name,gender=gender,age=age)
	obj.save()
	return HttpResponseRedirect(reverse('project:index'))

def signup(request):
	return render(request, 'app/signup.html')


def test3(request):

	req=urllib2.Request("http://127.0.0.1:8000/project/household")
	opener=urllib2.build_opener()
	f=opener.open(req)
	l=json.loads(f.read())
	j1=[]
	j2=[]
	j3=[]
	j4_lat=[]
	j4_long=[]
#print 'Name:',l[0]['name']
	for i in l:
		p=[]
		p.append(str(i['id']))
		p.append(i['latitude'])
		p.append(i['longitude'])
		j1.append(p)
		
	req=urllib2.Request("http://127.0.0.1:8000/project/point")
	opener=urllib2.build_opener()
	f=opener.open(req)
	l1=json.loads(f.read())

	req=urllib2.Request("http://127.0.0.1:8000/project/farm")
	opener=urllib2.build_opener()
	f=opener.open(req)
	l2=json.loads(f.read())

	req=urllib2.Request("http://127.0.0.1:8000/project/member")
	opener=urllib2.build_opener()
	f=opener.open(req)
	l3=json.loads(f.read())

	for k in l2:
		j2.append(k['area'])

	for m in l3:
		j3.append(str(m['name']))

	
	for i in range(len(j2)):
		p=[]	
		o=[]
		for j in l1:
			if j['F_id'] == (i+1):
				p.append(j['P_lat'])
				o.append(j['P_long'])
		j4_lat.append(p)
		j4_long.append(o)

	context={'j1':j1, 'j2':j2, 'j3':j3, 'j4_lat':j4_lat,'j4_long':j4_long}
	return render(request, 'project/test3.html',context)

