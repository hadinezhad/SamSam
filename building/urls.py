from django.conf.urls import url
from . import views
# building/
app_name = 'building'
urlpatterns = [

    url(r'^$', views.building, name="building"),
    url(r'^create/$', views.CreateBuildingFormView.as_view(), name="createBuilding"),
    url(r'^(?P<building_id>[0-9]+)/$', views.showdash, name="showdash"),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.DeleteBuilding.as_view(), name="deleteBuilding"),
    url(r'^activities/$', views.activities, name="activities"),
    url(r'^inbox/$', views.inbox, name="inbox"),
    url(r'^(?P<building_id>[0-9]+)/unit/$', views.unit, name="unit"),
    url(r'^(?P<building_id>[0-9]+)/unit/create/$', views.CreateUnitFormView.as_view(), name="createUnit"),
    # url(r'^(?P<building_id>[0-9]+)/neighbor/$', views., name="neighbor"),

]
