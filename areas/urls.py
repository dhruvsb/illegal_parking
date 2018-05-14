from django.urls import path, include
from django.conf.urls import url

from . import views

app_name="areas"

urlpatterns = [
    path(r'', views.ListCreateArea.as_view(), name='area_list'),
    path('<int:pk>/', views.RetrieveUpdateDestroyArea.as_view(), name='course_detail'),
    url(r'^(?P<area_pk>\d+)/images/$',
        views.ListCreateImage.as_view(),
        name='image_list'),
    url(r'^(?P<area_pk>\d+)/images/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyImage.as_view(),
        name='image_detail'),
]
