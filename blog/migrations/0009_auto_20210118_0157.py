# Generated by Django 3.1.5 on 2021-01-18 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210118_0155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'get_latest_by': ['order_date'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]
