# Generated by Django 3.0.4 on 2020-03-30 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Binaries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('binary_file', models.FileField(upload_to='')),
                ('remark', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
