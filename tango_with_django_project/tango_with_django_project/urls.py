from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(' ',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^tango_with_django_project/', include('tango_with_django_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^rango/', include('rango.urls')), # this new tuple maps to my applications urls.py module
    # The above mapping looks for url strings that match the patterns ^rango/
    # When a match is made the reaminder of th eurl string is then passed onto
    # and handled by rango.urls thanks to the include function
    url(r'^rango/about/', include('rango.urls'))
    # Why does this work?
    # Because Django looks up 'tango_with_django_project' we then say find /rango/
    # at the end of it then find /about/ at the end of that. If it is there, then include the
    # urls.py module from the rango directory
)
