# Generated by Django 5.0.1 on 2024-02-06 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0008_category_image_category_is_popular_product_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='related_product',
            field=models.ManyToManyField(blank=True, null=True, related_name='related_product', to='catalogue.product'),
        ),
    ]
