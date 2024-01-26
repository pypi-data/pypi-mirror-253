from django.contrib import admin
from .models import *

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    model = Page
    list_filter = ('site',)

@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    model = Text
    list_display = ('key', 'page', )
    list_filter = ('page', 'page__site')

@admin.register(FileData)
class FileDataAdmin(admin.ModelAdmin):
	list_display = ('id', 'file', 'description', 'uploaded_at',)
	readonly_fields=['uploaded_at']
	search_fields = ['description']
	list_filter = ('description',)
	ordering = ('-uploaded_at', )

@admin.register(ImageData)
class ImageDataAdmin(admin.ModelAdmin):
	list_display = ('id', 'file', 'description', 'uploaded_at',)
	readonly_fields=['uploaded_at']
	search_fields = ['description']
	list_filter = ('description',)
	ordering = ('-uploaded_at', )
