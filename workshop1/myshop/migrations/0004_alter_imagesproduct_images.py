# Generated by Django 3.2.4 on 2022-05-23 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0003_alter_imagesproduct_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagesproduct',
            name='images',
            field=models.FileField(upload_to='products/'),
        ),
    ]
