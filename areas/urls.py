from django.urls import path, include

from . import views

urlpatterns = [
    path(r'', views.area_list, name='list'),
    path('<int:pk>/', views.area_detail, name='detail'),
]
