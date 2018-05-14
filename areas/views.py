from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from . import models
from . import serializers


class ListCreateArea(generics.ListCreateAPIView):
    queryset = models.Area.objects.all()
    serializer_class = serializers.AreaSerializer


class RetrieveUpdateDestroyArea(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Area.objects.all()
    serializer_class = serializers.AreaSerializer


class ListCreateImage(generics.ListCreateAPIView):
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer

    def get_queryset(self):
        return self.queryset.filter(area_id=self.kwargs.get('area_pk'))

    def perform_create(self, serializer):
        area = get_object_or_404(
            models.Area, pk=self.kwargs.get('area_pk'))
        serializer.save(area=area)


class RetrieveUpdateDestroyImage(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            area_id=self.kwargs.get('area_pk'),
            pk=self.kwargs.get('pk')
        )


class AreaViewSet(viewsets.ModelViewSet):
    queryset = models.Area.objects.all()
    serializer_class = serializers.AreaSerializer

    @detail_route(methods=['get'])
    def images(self, request, pk=None):
        area = self.get_object()
        serializer = serializers.ImageSerializer(
            area.images.all(), many=True)
        return Response(serializer.data)


class ImageViewSet(viewsets.ModelViewSet):
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer
