from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.course_app.urls')),
]
