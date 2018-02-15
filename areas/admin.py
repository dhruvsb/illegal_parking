from django.contrib import admin

from .models import Area, Image


class ImageInline(admin.StackedInline):
    model = Image


class AreaAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]
    search_fields = ['name']

    list_filter = ['pincode']
    list_display = ['name', 'operator']


class ImageAdmin(admin.ModelAdmin):
    list_filter = ['fined', 'created_at']
    list_display = ['image_id', 'area', 'assessed']

    radio_fields = {'area': admin.HORIZONTAL}


admin.site.register(Area, AreaAdmin)
admin.site.register(Image, ImageAdmin)
