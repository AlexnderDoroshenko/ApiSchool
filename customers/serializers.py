from rest_framework import serializers
from .models import Clients, Stores, Poi, File, Binaries, Snippet
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']

class ClientsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'


class StoresDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stores
        fields = '__all__'


class PoiDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poi
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model = File
        fields = ('file', 'remark', 'timestamp')


class BinariesSerializer(serializers.ModelSerializer):
    class Meta():
        model = Binaries
        fields = ('binary_file', 'timestamp')