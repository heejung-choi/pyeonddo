from django.contrib import admin
from .models import Product, Post
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Post)