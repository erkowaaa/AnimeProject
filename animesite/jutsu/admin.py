from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


@admin.register(Anime)
class AnimeAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),

        }


admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Type)
admin.site.register(Ozvuchka)
admin.site.register(Director)
admin.site.register(Rating)
admin.site.register(Review)


