# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Member, Household, Photo, Audio,Farm, Point, Cropping, Well, Wellyield

# Register your models here.
admin.site.register(Member)
admin.site.register(Household)
admin.site.register(Photo)
admin.site.register(Audio)
admin.site.register(Farm)
admin.site.register(Point)
admin.site.register(Cropping)
admin.site.register(Well)
admin.site.register(Wellyield)