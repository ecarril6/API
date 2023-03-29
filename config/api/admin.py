from django.contrib import admin
from api.models import preProcessedImages, newTable


# Register your models here.
admin.site.register(newTable)
admin.site.register(preProcessedImages)
