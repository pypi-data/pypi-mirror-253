from modeltranslation.translator import register, TranslationOptions
from .models import Text, Page


@register(Text)
class TextTranslationOptions(TranslationOptions):
    fields = ('content', )


@register(Page)
class PageTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )