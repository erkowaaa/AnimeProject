from rest_framework import serializers
from .models import *


class AnimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['anime_name', 'category', 'genre', 'type', 'ozvuchka', 'director', 'description', 'published_date', 'image', 'popular']


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class OzvuchkaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ozvuchka
        fields = '__all__'


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'