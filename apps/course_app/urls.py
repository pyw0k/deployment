from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^add_course$', views.add_course, name='add'),
    url(r'^destroy/(?P<id>\d+)', views.destroy, name='destroy'),
]
