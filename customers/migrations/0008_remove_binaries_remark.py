# Generated by Django 3.0.4 on 2020-03-30 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_auto_20200330_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='binaries',
            name='remark',
        ),
    ]
