from django.contrib import admin
from .models import Store
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
# Register your models here.

class StoreAdmin(ImportExportMixin, admin.ModelAdmin):
    pass
admin.site.register(Store,StoreAdmin)
