# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import datetime

# Create your models here.
class Household(models.Model):
	
	latitude = models.FloatField()
	longitude = models.FloatField()
	income = models.IntegerField()
	area = models.FloatField()

	def __unicode__(self):

		return "%s"%(self.id)


class Member(models.Model):

	H_id = models.ForeignKey(Household, on_delete = models.CASCADE)
	name = models.CharField(max_length = 200)
	gender_choices=(('M', 'Male'), ('F', 'Female'),)
	gender = models.CharField(max_length=1, choices = gender_choices)
	age = models.IntegerField()

	def __str__(self):

		return self.name

class Photo(models.Model):

	H_id = models.ForeignKey(Household, on_delete = models.CASCADE)
	url = models.URLField()

	def __str__(self):
		return self.url

class Audio(models.Model):

	H_id = models.ForeignKey(Household, on_delete = models.CASCADE)
	clips = models.FilePathField()


class Farm(models.Model):

	H_id = models.ForeignKey(Household, on_delete = models.CASCADE)
	area = models.FloatField()

	def __unicode__(self):

		return "%s"%(self.id)

class Point(models.Model):

	F_id = models.ForeignKey(Farm, on_delete = models.CASCADE)
	P_lat = models.FloatField()
	P_long = models.FloatField()

	def __unicode__(self):

		return "%s"%(self.F_id)


class Crop(models.Model):

	name = models.CharField(max_length = 50)


class Cropping(models.Model):

	F_id = models.ForeignKey(Farm, on_delete = models.CASCADE)
	crop_id = models.ForeignKey(Crop, on_delete= models.CASCADE)
	season_id = models.IntegerField()
	c_year = models.DateTimeField()
	c_area = models.FloatField()

class Well(models.Model):

	F_id = models.ForeignKey(Farm, on_delete = models.CASCADE)
	w_lat = models.FloatField()
	w_long = models.FloatField()
	well_water_depth = models.FloatField()
	avg_wateryield = models.FloatField()

	def __unicode__(self):

		return "%s"%(self.id)

class Wellyield(models.Model):

	well_id = models.ForeignKey(Well, on_delete = models.CASCADE)
	water_depth = models.FloatField()
	date = models.DateField(null = True)
	wateryield = models.FloatField()

	def __unicode__(self):

		return "%s"%(self.well_id)