from django.db import models


class Area(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    area_id = models.IntegerField(default=100)
    operator = models.CharField(max_length=255)
    operator_id = models.IntegerField(default=1)
    pincode = models.IntegerField(default=395001)

    def __str__(self):
        return self.name


class Image(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    image_id = models.CharField(default="img1001", max_length=10)
    image = models.FileField(null=True, blank=True)
    number_plate = models.CharField(max_length=255, default="GJ-05-7777")
    coordinates = models.CharField(max_length=255)
    assessed = models.BooleanField(default=False)
    fined = models.BooleanField(default=False)
    sender_id = models.IntegerField(default=200)
    area = models.ForeignKey('Area', on_delete=models.CASCADE)

    def __str__(self):
        return self.image_id
