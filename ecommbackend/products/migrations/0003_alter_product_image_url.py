# Generated by Django 4.1.5 on 2023-01-24 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.FileField(default='pics/400x300.png', upload_to='product_images'),
        ),
    ]
