# Generated by Django 4.1.5 on 2023-01-11 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
