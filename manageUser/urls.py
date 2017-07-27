from django.conf.urls import url
from . import views
# home/
app_name = 'manageUser'
urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^login/$', views.login, name="login"),
    url(r'^guide/$', views.guide, name="guide"),
    url(r'^callus/$', views.callus, name="callus"),



]
