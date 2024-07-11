from .serializers import *
from .models import *
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .filter import AnimeFilter
from rest_framework.filters import SearchFilter


class AnimeViewSets(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = AnimeFilter
    search_fields = ['anime_name']
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class GenreViewSets(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers


class TypeViewSets(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializers


class OzvuchkaViewSets(viewsets.ModelViewSet):
    queryset = Ozvuchka.objects.all()
    serializer_class = OzvuchkaSerializers


class DirectorViewSets(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializers


class UserProfileViewSets(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers


class ReviewViewSets(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers


class RatingViewSets(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers

