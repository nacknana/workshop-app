# Generated by Django 3.2.4 on 2022-05-23 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0004_alter_imagesproduct_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
        migrations.AlterField(
            model_name='imagesproduct',
            name='images',
            field=models.FileField(upload_to='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='myshop.category'),
        ),
    ]
