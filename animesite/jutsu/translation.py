from django.contrib import admin
from .models import *
from modeltranslation.translator import TranslationOptions, register



@register(Anime)
class BookTranslationOptions(TranslationOptions):
    fields = ('anime_name',)

