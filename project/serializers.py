from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Member, Household, Photo, Audio, Farm, Cropping, Point, Well, Wellyield

class HouseholdSerializer(serializers.ModelSerializer):

	class Meta:
		model = Household
		fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):

	class Meta:
		model = Member
		fields = '__all__'

class AudioSerializer(serializers.ModelSerializer):

	class Meta:
		model = Audio
		fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Photo
		fields = '__all__'


class FarmSerializer(serializers.ModelSerializer):

	class Meta:
		model = Farm
		fields = '__all__'


class CroppingSerializer(serializers.ModelSerializer):

	class Meta:
		model = Cropping
		fields = '__all__'


class PointSerializer(serializers.ModelSerializer):

	class Meta:
		model = Point
		fields = '__all__'

class WellSerializer(serializers.ModelSerializer):

	class Meta:
		model = Well
		fields = '__all__'

class WellyieldSerializer(serializers.ModelSerializer):

	class Meta:
		model = Wellyield
		fields = '__all__'