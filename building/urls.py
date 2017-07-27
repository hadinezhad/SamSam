from django.conf.urls import url
from . import views
# building/
app_name = 'building'
urlpatterns = [

    url(r'^$', views.building, name='building'),
    url(r'^(?P<building_id>[0-9]+)/$', views.showDash, name="showDash"),

]