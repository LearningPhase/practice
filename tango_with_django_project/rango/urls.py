from django.conf.urls import patterns, url
# figure out what the modules/directory and the function do
from rango import views
# importing our view module from the rango directory
# allows the functions below to access our views for reference in the URL mapping

urlpatterns = patterns(' ',
                      url(r'^$', views.index, name='index'),
                      url(r'^about/', views.about, name='about')) # must move the end parenthesis on the tuple
