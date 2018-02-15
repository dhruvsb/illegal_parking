from django.http import HttpResponse
from django.shortcuts import render

from .models import Area, Image


def area_list(request):
    areas = Area.objects.all()
    return render(request, 'areas/area_list.html', {'areas': areas})


def area_detail(request, pk):
    area = Area.objects.get(pk=pk)
    return render(request, 'areas/area_detail.html', {'area': area})
