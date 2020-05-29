from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


class Snippet(models.Model):
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

class Binaries(models.Model):
    binary_file = models.BinaryField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

# Create your models here.
class File(models.Model):
  file = models.FileField(blank=False, null=False)
  remark = models.CharField(max_length=20)
  timestamp = models.DateTimeField(auto_now_add=True)

class Stores(models.Model):
    store_id  = models.IntegerField(verbose_name='Store_Id', primary_key=True, unique=True,  db_index=True)
    store_name = models.CharField(verbose_name='Store_Name', max_length= 64)
    store_description = models.CharField(verbose_name='Store_Description', max_length=64)
    STORE_TYPE = (
        (1, 'DutyFree'),
        (2, 'WithVat'),
        (0, 'Undefined'),
    )
    store_type = models.IntegerField(verbose_name='Store_Type', choices=STORE_TYPE)

class Clients(models.Model):
    id = models.IntegerField(verbose_name='Id',primary_key=True, unique=True,  db_index=True)
    name = models.CharField(verbose_name='Name', max_length= 64)
    last_name = models.CharField(verbose_name='Last_Name', max_length=64)
    SEX = (
        (1, 'Male'),
        (2, 'Famale'),
        (0, 'Undefined'),
    )
    sex = models.IntegerField(verbose_name='Customer_Sex', choices=SEX)
    CLIENTS_TYPE = (
        (1, 'Vendor'),
        (2, 'Customer'),
        (0, 'Undefined'),
    )
    type = models.IntegerField(verbose_name='Clients_Type', choices=CLIENTS_TYPE)

class Poi(models.Model):
    poi_id = models.IntegerField(verbose_name='POI_Id', primary_key=True, unique=True, db_index=True)
    net_number = models.IntegerField(verbose_name='Net_Number',  db_index=True)
    store_number = models.IntegerField(verbose_name='Store_Number', db_index=True)