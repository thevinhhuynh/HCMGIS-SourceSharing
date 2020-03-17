from django.conf.urls import patterns, include, url

from django.contrib import admin
from onlinecounter import views as onlinecounter_views
admin.autodiscover()

urlpatterns = [
    url(r'^onlinecounter/', onlinecounter_views.main, name='onlinecounter_views_main),
    url(r'^admin/', include(admin.site.urls)),
]
