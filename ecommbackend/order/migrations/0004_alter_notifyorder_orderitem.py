# Generated by Django 4.1.5 on 2023-01-20 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_customer_alter_orderitem_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifyorder',
            name='orderItem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.orderitem'),
        ),
    ]