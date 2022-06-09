from django.db import models
from django.utils.html import format_html

# Create your models here.


class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    cat_image = models.FileField(
        upload_to='Categories', null=True, blank=True)
    cat_detail = models.TextField(null=True, blank=True, max_length=255,)
    cat_status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.cat_name

    def show_image(self):
        if self.cat_image:
            return format_html('<img src="' + self.cat_image.url + '" height="100px">')
        return ''
    show_image.allow_tags = True


class Product(models.Model):
    prod_name = models.CharField(max_length=250)
    # slug = models.SlugField(max_length=200, unique=True,defa)
    prod_category = models.ForeignKey(
        Category,  default=None, blank=True, null=True, on_delete=models.CASCADE)

    prod_detail = models.TextField(max_length=255, null=True, blank=True)

    # image = models.FileField(blank=True)
    prod_price = models.FloatField(default=0)
    prod_recommend = models.BooleanField(default=False)
    prod_status = models.BooleanField(default=False)
    prod_created = models.DateTimeField(auto_now_add=True)
    prod_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return str(self.prod_name)
# env อยู่ไหน


class ImagesProduct(models.Model):
    prod_id = models.ForeignKey(
        Product, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='Products')

    def __str__(self):
        return self.prod_id.prod_name

    def show_image_product(self):
        if self.images:
            return format_html('<img src="' + self.images.url + '" height="100px">')
        return ''
    show_image_product.allow_tags = True


class Contact(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    e_mail = models.EmailField(max_length=70)
    message = models.TextField(max_length=255, null=True, blank=True)


class Comment(models.Model):
    product_comment = models.ForeignKey(
        Product, default=None, on_delete=models.CASCADE, related_name='comments')
    message = models.TextField(max_length=500, null=True, blank=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.message
