# Generated by Django 4.2.2 on 2023-06-18 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_third_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='fifth_image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/products'),
        ),
        migrations.AddField(
            model_name='product',
            name='fourth_image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/products'),
        ),
    ]