from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.db.models import ManyToOneRel, ForeignKey, OneToOneField
# Register your models here.
@admin.register(Poi)
class poiAdmin(admin.ModelAdmin):
    list_display = ("poi_id", "store_number", "net_number")


@admin.register(Clients)
class clientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "last_name", "SEX", "CLIENTS_TYPE")

@admin.register(Stores)
class storeAdmin(admin.ModelAdmin):
    list_display = ("store_id", "store_name", "store_description", "STORE_TYPE")

@admin.register(Snippet)
class snippetAdmin(admin.ModelAdmin):
    list_display = ("owner", "highlighted")

@admin.register(File)
class filesAdmin(admin.ModelAdmin):
    list_display = ("file", "remark", "timestamp")


@admin.register(Binaries)
class binariesAdmin(admin.ModelAdmin):
    list_display = ("binary_file", "timestamp")

MySpecialAdmin = lambda model: type('SubClass'+model.__name__, (admin.ModelAdmin,), {
    'list_display': [x.name for x in model._meta.fields],
    'list_select_related': [x.name for x in model._meta.fields if isinstance(x, (ManyToOneRel, ForeignKey, OneToOneField,))]
})

admin.site.unregister(User)
admin.site.register(User, MySpecialAdmin(User))