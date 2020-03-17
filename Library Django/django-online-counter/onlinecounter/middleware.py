#-*- coding:utf-8 -*-
#Copyright (C) 2020, thevinhhuynh

from django.utils.deprecation import MiddlewareMixin
from onlinecounter.models import OnlineCounter
from datetime import datetime, time

class OnlineCounterMiddleware(MiddlewareMixin):
    def process_request(self, request):
        now_time = datetime.now().time()
        limit = time(now_time.hour, now_time.minute-5, now_time.second, now_time.microsecond)
        OnlineCounter.objects.filter(visited_time__lt=limit).delete()
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ips = x_forwarded_for.split(',')[-1].strip()
        elif request.META.get('HTTP_X_REAL_IP'):
            ips = request.META.get('HTTP_X_REAL_IP')
        else:
            ips = request.META.get('REMOTE_ADDR')
        print ips
        online, create = OnlineCounter.objects.get_or_create(
            ip=ips
        )
        if request.user.is_authenticated():
            online.is_user = True
        if not create:
            online.is_user = False
            online.visited_time = now_time
            online.save()
        request.online = self

    def total(self):
        total = OnlineCounter.objects.all().count()
        return total

    def guest(self):
        guest = OnlineCounter.objects.filter(is_user=False).count()
        return guest

    def users(self):
        users = OnlineCounter.objects.filter(is_user=True).count()
        return users