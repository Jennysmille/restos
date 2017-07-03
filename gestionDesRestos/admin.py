# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Restos, Menu, Plats
admin.site.register(Restos)
admin.site.register(Menu)
admin.site.register(Plats)
