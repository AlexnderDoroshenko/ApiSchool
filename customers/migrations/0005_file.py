# Generated by Django 3.0.4 on 2020-03-29 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_poi_store_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('remark', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
