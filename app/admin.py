from django.contrib import admin
from .models import Image
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class ImageResource(resources.ModelResource):
    class Meta:
        model = Image


class ImageAdmin(ImportExportModelAdmin):
    resource_class = ImageResource

admin.site.register(Image, ImageAdmin)