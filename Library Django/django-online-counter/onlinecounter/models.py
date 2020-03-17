#-*- coding:utf-8 -*-

#Copyright (C) 2020, thevinhhuynh

from django.db import models

class OnlineCounter(models.Model):
    ip = models.GenericIPAddressField(verbose_name="IP Adress", db_column="visitor_ip")
    is_user = models.BooleanField(verbose_name="User ?", db_column="is_user", default=False)
    visited_time = models.TimeField(verbose_name="Visited Time", db_column="visitor_time", auto_now_add=True)

    class Meta:
        db_table = "online_counter"
        verbose_name_plural = "Online Counter"
