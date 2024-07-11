from django.urls import path
from .views import *

urlpatterns = [
    path('', AnimeViewSets.as_view({'get': 'list', 'post': 'create'}), name = 'anime_list'),
    path('<int:pk>/', AnimeViewSets.as_view({'get': 'retrieve', 'put': 'update',
                                               'delete': 'destroy'}), name = 'anime_detail'),

    path('userProfile/', UserProfileViewSets.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('userProfile/<int:pk>/', UserProfileViewSets.as_view({'get': 'retrieve', 'put': 'update',
                                               'delete': 'destroy'}), name='user_detail'),

    path('category/', CategoryViewSets.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('category/<int:pk>/', CategoryViewSets.as_view({'get': 'retrieve', 'put': 'update',
                                               'delete': 'destroy'}), name='category_detail'),

    path('genre/', GenreViewSets.as_view({'get': 'list', 'post': 'create'}), name='genre_list'),
    path('genre/<int:pk>/', GenreViewSets.as_view({'get': 'retrieve', 'put': 'update',
                                               'delete': 'destroy'}), name='genre_detail'),

    path('type/', TypeViewSets.as_view({'get': 'list', 'post': 'create'}), name='type_list'),
    path('type/<int:pk>/', AnimeViewSets.as_view({'get': 'retrieve', 'put': 'update',
                                               'delete': 'destroy'}), name='anime_detail'),

    path('category/', CategoryViewSets.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('category/<int:pk>/', CategoryViewSets.as_view({'get': 'retrieve', 'put': 'update',
                                               'delete': 'destroy'}), name='category_detail'),

    path('ozvuchka/', OzvuchkaViewSets.as_view({'get': 'list', 'post': 'create'}), name='ozvuchka_list'),
    path('ozvuchka/<int:pk>/', OzvuchkaViewSets.as_view({'get': 'retrieve', 'put': 'update',
                                               'delete': 'destroy'}), name='ozvuchka_detail'),

    path('review/', ReviewViewSets.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('review/<int:pk>/', ReviewViewSets.as_view({'get': 'retrieve', 'put': 'update',
                                               'delete': 'destroy'}), name='review_detail'),

    path('rating/', RatingViewSets.as_view({'get': 'list', 'post': 'create'}), name='rating_list'),
    path('rating/<int:pk>/', RatingViewSets.as_view({'get': 'retrieve', 'put': 'update',
                                                     'delete': 'destroy'}), name='rating_detail'),
]