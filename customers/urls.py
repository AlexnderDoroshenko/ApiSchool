from django.urls import path, include, re_path
from .views import *
from rest_auth.registration.views import VerifyEmailView, RegisterView
from rest_framework_jwt.views import obtain_jwt_token as ojt

app_name = 'customers'

urlpatterns = [
    path('', start, name='start'),
    path('api/v1/users/', UserList.as_view()),
    path('api/v1/users/<int:pk>/', UserDetail.as_view()),
    path('api/v1/', index, name='index'),
    path('api/v1/resources/', resources, name='resources'),
    path('api/v1/methods/', methods, name='methods'),
    path('api/v1/client/details/<int:pk>', ClientDetailView.as_view()),
    path('api/v1/client/create/', ClientCreateView.as_view(), name='client/create/'),
    path('api/v1/store/details/<int:pk>', StoreDetailView.as_view()),
    path('api/v1/store/create/', StoreCreateView.as_view(), name='store/create/'),
    path('api/v1/poi/details/<int:pk>', PoiDetailView.as_view()),
    path('api/v1/poi/create/', PoiCreateView.as_view(), name='poi/create/'),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/v1/upload/', FileView.as_view(), name='file-upload'),
    path('api/v1/binary/', BinaryView.as_view(), name='file-upload'),


    ]

urlpatterns += [
    path('api/v1/api-token-auth/', ojt),
    path('api/v1/rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login')
]