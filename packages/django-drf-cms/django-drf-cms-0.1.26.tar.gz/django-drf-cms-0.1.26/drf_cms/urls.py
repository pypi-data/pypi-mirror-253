from django.urls import path
from .views import *

urlpatterns = [
    path('pages/<str:page_key>/texts/', TextView.as_view(), name='text-list'),
    path('pages/<str:page_key>/texts/<str:key>/', TextView.as_view(), name='text-obj'),
    path('pages/<str:key>/', PageView.as_view(), name='page-list'),
    path('pages/', PageView.as_view(), name='page-obj'),
    path('files', FileUploadView.as_view(), name = 'file_upload'),
	path('files/signed', SignedUrlView.as_view(), name = 'get_signed'),
    path('images/upload', ImageUploadView.as_view(), name = 'image_upload'),
]
