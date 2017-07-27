from django.conf.urls import url
from . import views
# home/
urlpatterns = [

    url(r'^$', views.home, name='home'),

]
