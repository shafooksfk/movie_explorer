from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from movie_app.models import Movie, Rating

from . import services

import requests
# Create your views here.

def index(request):
    query = request.GET.get('q')
    
    movie_data = services.fetchMovies(query)
    
    if 'error' in movie_data:
       context = {
           'error_message':movie_data['error'],
           'query': query if query else 'Popular Movies',
           'movie_data': [],
           'page_number': 1,
       }
    elif query:
        context = {
            'query': query,
            'movie_data': movie_data,
            'page_number': 1,
        }
        return render(request, 'search_results.html', context)
    else:
        context = {
            'query':'Popular Movies',
            'movie_data':movie_data,
            'page_number':1,
        }
    return render(request, 'index.html', context)

       

def pagination(request, query, page_number):
    
    movie_data, page_number, error= services.fetchMoviesWithPagination(query,page_number)
    
    if error:
        context = {
            'query': query,
            'movie_data': [],  
            'error': error,
            'page_number': page_number,
        }
        
    context = {
		'query': query,
		'movie_data': movie_data,
		'page_number': page_number,
	}
    

    return render(request, 'search_results.html', context)


def movieDetails(request,imdb_id):
    
    movie_data, ourdb_or_error = services.fetchMovieDetails(imdb_id)

    if ourdb_or_error is True:
        context = {
            'movie_data': movie_data,
            'ourdb': True,
        }
    elif ourdb_or_error is False:
        context = {
            'movie_data': movie_data,
            'ourdb': False,
        }
    else:
        context = {
            'error': ourdb_or_error,
            'movie_data': None,
            'ourdb': False,
        }

    return render(request, 'movie_details.html', context)
 