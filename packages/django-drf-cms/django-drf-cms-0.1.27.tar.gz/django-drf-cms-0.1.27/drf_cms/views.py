from django.shortcuts import render, redirect
from django.conf import settings
from rest_framework import generics, mixins, status
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Text, FileData, ImageData
from .forms import ImageUpload
from .serializers import *
from .permissions import IsOwnerOrReadOnly
from .shortcuts import get_current_site
from .storage_backends import create_presigned_post


class TextView(
		mixins.ListModelMixin, 
		mixins.RetrieveModelMixin,
		mixins.UpdateModelMixin,
		generics.GenericAPIView):
	serializer_class = TextSerializer
	permission_classes = [IsOwnerOrReadOnly]
	lookup_field = 'key'

	def get_queryset(self):
		page_key = self.kwargs.get('page_key')
		site = get_current_site(self.request)
		return Text.objects.filter(page__key=page_key, page__site=site)

	def get(self, request, *args, **kwargs):
		key = self.kwargs.get('key')
		if (key):
			return self.retrieve(request, *args, **kwargs)
		return self.list(request, *args, **kwargs)

	def patch(self, request, *args, **kwargs):
		return self.partial_update(request, *args, **kwargs)



class PageView(
		mixins.ListModelMixin,
		mixins.RetrieveModelMixin,
		generics.GenericAPIView):
	serializer_class = PageSerializer
	permission_classes = [IsOwnerOrReadOnly]
	lookup_field = 'key'

	def get_queryset(self):
		site = get_current_site(self.request)
		return Page.objects.filter(site=site)

	def get(self, request, *args, **kwargs):
		key = self.kwargs.get('key')
		if (key):
			return self.retrieve(request, *args, **kwargs)
		return self.list(request, *args, **kwargs)


class FileUploadView(APIView):
    permission_classes = [IsAdminUser]
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
      file = None
      url = request.data.get('url', None)
      description = request.data.get('description', '')
      if url:
        file = FileData.objects.create()
        file.file.name = url.lower()
        file.description = description
        file.save()
      else:
        file_serializer = FileDataSerializer(data=request.data)

        if file_serializer.is_valid():
            file = file_serializer.save()
          
      if file:
          print(FileDataSerializer(file).data)
          return Response(FileDataSerializer(file).data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignedUrlView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, *args, **kwargs):
      filename = request.GET.get('filename', None)
      if not filename:
        return Response(
          {'message': 'missing url param filename'}, 
          status=status.HTTP_400_BAD_REQUEST)
      
      response = create_presigned_post(
        settings.AWS_STORAGE_BUCKET_NAME, 
        filename)

      if not response:
        return Response(
          {'message': 'Error signing url'}, 
          status=status.HTTP_503_SERVICE_UNAVAILABLE)
      return Response(response, status=status.HTTP_200_OK)


class ImageUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = ImageDataSerializer(data=request.data)

      if file_serializer.is_valid():
        file_serializer.save()
        return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

