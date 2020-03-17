#-*- coding:utf-8 -*-
#Copyright (C) 2020, thevinhhuynh

from onlinecounter.models import OnlineCounter
from django.contrib import admin

class OnlineCounterAdmin(admin.ModelAdmin):
    list_display = ("ip",)
    exlude = ("ip",)
    readonly_fields = ("ip",)

admin.site.register(OnlineCounter, OnlineCounterAdmin)
