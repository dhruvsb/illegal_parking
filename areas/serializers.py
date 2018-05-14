from rest_framework import serializers

from . import models


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'image_id',
            'image',
            'number_plate',
            'coordinates',
            'assessed',
            'fined',
            'sender_id',
            'area',
            'created_at'
        )
        model = models.Image


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'area_id',
            'operator',
            'operator_id',
            'pincode'
        )
        model = models.Area
