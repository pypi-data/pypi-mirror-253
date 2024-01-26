from rest_framework import serializers
from .models import Page, Text, FileData, ImageData
import pathlib
from django.conf import settings
from urllib.parse import urlparse


class TextSerializer(serializers.ModelSerializer):
    key = serializers.CharField(read_only=True)

    class Meta:
        model = Text
        fields = ('content', 'key')


class PageSerializer(serializers.ModelSerializer):
    texts = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Page
        fields = ('key', 'title', 'description', 'texts')

    def get_texts(self, instance):
        texts = instance.text_set.all()
        result = {}
        for text in texts:
            result[text.key] = text.content
        return result


class FileDataSerializer(serializers.ModelSerializer):
	file = serializers.FileField()
	extra = serializers.SerializerMethodField()

	class Meta:
		model = FileData
		fields = ('file', 'id', 'description', 'extra')

	def get_extra(self, instance):
		if not instance.file:
			return None
		if (pathlib.Path(instance.file.url).suffix.lower() == '.mp4'):
			url = urlparse(instance.file.url)
			filename = pathlib.Path(url.path).stem
			base_url = 'https://{}.s3.amazonaws.com/{}'.format(
				settings.AWS_STORAGE_VIDEO_BUCKET_NAME, filename)
			file = {
				'hls': '{}/HLS/{}.m3u8'.format(base_url, filename),
				'thumbnail': '{}/Thumbnails/{}.0000004.jpg'.format(
								base_url, filename),
				'thumbnail_fallback': '{}/Thumbnails/{}.0000002.jpg'.format(
								base_url, filename)
			}
			return file
		return None


class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = ImageData
		fields = ('url', 'id', 'description', 'width', 'height')