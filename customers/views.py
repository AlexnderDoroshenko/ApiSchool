from rest_framework import generics
from .serializers import StoresDetailSerializer, ClientsDetailSerializer, PoiDetailSerializer, UserSerializer
from .models import Clients, Stores, Poi
from django.shortcuts import render, redirect
from rest_framework.parsers import JSONParser, FileUploadParser
import os
from rest_auth.registration.views import RegisterView
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status, renderers
from .serializers import FileSerializer, BinariesSerializer
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BinaryView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        file_serializer = BinariesSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save(os.path.join(files_dir, filename))
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileUploadView(APIView):
    parser_classes = [FileUploadParser]
    def put(self, request, filename, format=None):
        if request.method == "POST":
            file_obj = request.data['file']
            files_dir = "ApiSchool/files/"
            file_obj.save(os.path.join(files_dir, filename))
            return Response(status=204)
        else:
            return Response(status=405)


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientsDetailSerializer
    queryset = Clients.objects.all()


class StoreDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StoresDetailSerializer
    queryset = Stores.objects.all()


class PoiDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PoiDetailSerializer
    queryset = Poi.objects.all()


class ClientCreateView(generics.CreateAPIView):
    serializer_class = ClientsDetailSerializer
    lookup_url_kwarg = "uid"

    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_url_kwarg)
        client_info = Clients.objects.filter(article=uid)
        return client_info


class StoreCreateView(generics.CreateAPIView):
    serializer_class = StoresDetailSerializer


class PoiCreateView(generics.CreateAPIView):
    serializer_class = PoiDetailSerializer

def index(request):
    if User.is_authenticated:
        return render(request, 'includes/homePage.html')
    else:
        return Response(status=403)


def resources(request):
    return render(request, 'includes/resources.html')

def methods(request):
    return render(request, 'includes/methods.html')

def start(request):
    return redirect('api/v1/')