# Generated by Django 3.2.4 on 2022-05-23 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0002_auto_20220523_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagesproduct',
            name='images',
            field=models.FileField(upload_to='images/products/'),
        ),
    ]
