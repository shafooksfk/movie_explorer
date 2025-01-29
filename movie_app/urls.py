from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('search/<query>/page/<page_number>',views.pagination,name='pagination'),
    path('<imdb_id>',views.movieDetails,name='movie-details')
] 