# Generated by Django 4.1.5 on 2023-01-19 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderTotalPrice',
            field=models.FloatField(null=True),
        ),
    ]
