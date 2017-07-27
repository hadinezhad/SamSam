from django.conf.urls import url
from . import views
# building/
app_name = 'building'
urlpatterns = [

    url(r'^$', views.building, name='building'),
    url(r'^(?P<building_id>[0-9]+)/$', views.showdash, name="showdash"),
    url(r'^activities/$', views.activities, name="activities"),
    url(r'^inbox/$', views.inbox, name="inbox"),

]