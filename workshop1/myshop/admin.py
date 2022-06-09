from django.contrib import admin

from .models import *
from django.utils.html import format_html

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cat_name', 'show_image', 'cat_detail', 'cat_status']
    list_filter = ['cat_status']
    search_fields = ['cat_name']


class ImagesProductAdmin(admin.StackedInline):

    model = ImagesProduct
    extra = 4


# @admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['prod_name', 'display_img',
                    'prod_detail', 'prod_price', 'prod_recommend', 'prod_status', ]
    inlines = [ImagesProductAdmin]
    list_filter = ['prod_category', 'prod_status']
    search_fields = ['prod_name']

    def display_img(self, obj):
        imgs = ImagesProduct.objects.filter(prod_id=obj)
        print(imgs)
        div = '<div>'
        for img in imgs:
            div += '<img src="%s" style="border:2px solid black;border-radius:50px" height="100px"> <br/>' % img.images.url
        div += '<div>'
        return format_html(div)

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Contact)
