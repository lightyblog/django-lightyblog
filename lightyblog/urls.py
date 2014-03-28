#/////////////////////////////////////////////////////////////////
from django.conf.urls import patterns, include, url

#/////////////////////////////////////////////////////////////////
# Django Admin 
from django.contrib import admin
admin.autodiscover()

#/////////////////////////////////////////////////////////////////
# Lightyblog - App urls
urlpatterns = patterns('',
    url(r'^$', 'lightyblog.views.index',),
    url(r'^article/(?P<articleid>\d+)/$', 'lightyblog.views.article'),
    url(r'^latest-article/$', 'lightyblog.views.latest'),
    url(r'^admin/list-article/', 'lightyblog.views.list',),
    url(r'^admin/create-article/', 'lightyblog.views.create',),
    url(r'^admin/edit-article/(?P<articleid>\d+)/$', 'lightyblog.views.edit',),
    url(r'^admin/delte-article/(?P<articleid>\d+)/$', 'lightyblog.views.delete',),
)

#/////////////////////////////////////////////////////////////////
# Django Admin urls
urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'django.contrib.auth.views.login'),
)
 
