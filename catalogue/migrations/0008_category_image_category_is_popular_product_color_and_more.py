# Generated by Django 5.0.1 on 2024-02-06 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0007_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='category'),
        ),
        migrations.AddField(
            model_name='category',
            name='is_popular',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('Red', 'Red'), ('Green', 'Green'), ('Others', 'Others')], default='Others', max_length=40),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
        migrations.AddField(
            model_name='product',
            name='related_product',
            field=models.ManyToManyField(related_name='related_product', to='catalogue.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('xl', 'xl'), ('xxl', 'xxl'), ('Others', 'Others')], default=0, max_length=40),
        ),
    ]
