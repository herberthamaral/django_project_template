from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{project_name}}.views.home', name='home'),
    # url(r'^{{project_name}}/', include('{{project_name}}.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    if len(urlpatterns) == 0:
        from django.shortcuts import render
        def index(request):
            return render(request, 'index.html', {'project_name':'{{project_name}}'})
        urlpatterns += patterns('',url(r'^$', index))


    urlpatterns += patterns('',
            url('^media/(?P<path>.*)$', 
                'django.views.static.serve', 
                {'document_root':settings.MEDIA_ROOT}
               ),
    )
