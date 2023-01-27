# Generated by Django 4.1.5 on 2023-01-25 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_comments_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'comment'},
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name_plural': 'comments'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='star',
            field=models.CharField(choices=[(0, 'None'), (1, 'Very Bad'), (2, 'Bad'), (3, 'Not Bad'), (4, 'Good'), (5, 'Very Good')], default=0, max_length=40),
        ),
    ]