from django.db import models
from django_bleach.models import BleachField
from django.contrib.sites.models import Site
from .mixins import *


class Page(models.Model):
	site = models.ForeignKey(Site, null=False, on_delete=models.CASCADE)
	key = models.CharField(null=False, max_length=64)
	title = models.CharField(null=False, max_length=128)
	description = models.CharField(blank=True, max_length=256)

	class Meta:
		unique_together = ('site', 'key')

	def __str__(self):
		return '{} - {}'.format(self.key, self.site.domain)


class ContentMixin(models.Model):
	page = models.ForeignKey(Page, null=False, on_delete=models.CASCADE)
	key = models.CharField(null=False, max_length=64)

	class Meta:
		unique_together = ('page', 'key')
		abstract = True

	def __str__(self):
		return self.key


class MetadataMixin(models.Model):
	description = models.CharField(blank=True, max_length=512)
	uploaded_at =  models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True

	def __str__(self):
		return self.description


class ImageData(MetadataMixin):
	file = models.ImageField(height_field='height', width_field='width')
	height = models.PositiveIntegerField(default=0)
	width = models.PositiveIntegerField(default=0)

	@property
	def url(self):
		return self.file.url


class FileData(MetadataMixin):
	file = models.FileField()


class Text(ContentMixin):
	content = BleachField(null=False, allowed_tags=['a', 'p', 'i', 'b', 'u'], allowed_attributes=['href'])


class Image(ContentMixin):
	content = models.ForeignKey(ImageData, null=False, on_delete=models.PROTECT)

	@property
	def url(self):
		return self.content.url

	@property
	def width(self):
		return self.content.width

	@property
	def height(self):
		return self.content.height


class File(ContentMixin):
	content = models.ForeignKey(FileData, null=False, on_delete=models.PROTECT, related_name='file_data')
