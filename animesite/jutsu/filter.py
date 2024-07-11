from django_filters.rest_framework import FilterSet
from .models import *


class AnimeFilter(FilterSet):
    class Meta:
        model = Anime
        fields = {
            'anime_name': ['exact'],
            'genre': ['exact'],
            'type': ['exact'],
            'ozvuchka': ['exact'],
            'published_date': ['gt', 'lt'],

        }