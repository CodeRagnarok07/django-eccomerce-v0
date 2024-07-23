from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin, TabularInline, ModelAdmin
# Register your models here.

from .models import Product, Category, Collection, Variant, VariantGalery
from nested_admin import NestedTabularInline, NestedModelAdmin, NestedStackedInline


admin.site.register(Category)
admin.site.register(Collection)



class VariantGaleryInline(NestedTabularInline):
    model = VariantGalery
    classes = ['collapse']
    
    extra = 0

class VariantInline(NestedTabularInline):
    model = Variant
    extra = 0
    inlines = [VariantGaleryInline]
 
@admin.register(Product)
class ProductAdmin(NestedModelAdmin):
    inlines = [VariantInline]




