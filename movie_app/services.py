
from movie_app.models import Movie, Rating

import requests
import os

def fetchMovies(query = None):
    api_key = os.getenv('OMDB_API_KEY')
    try:
        if query:
            url = 'https://www.omdbapi.com/?apikey=' + api_key+ '&s=' + query
        else: 
            url = 'https://www.omdbapi.com/?apikey='+ api_key +'&s=batman' 
        response = requests.get(url)
        response.raise_for_status()
        
        movie_data= response.json()

        return movie_data
    
    except Exception as e:
        return {'error': f"An unexpected error occurred: {str(e)}"}
    
def fetchMoviesWithPagination(query,page_number):
    api_key = os.getenv('OMDB_API_KEY')
    try:
            
        url = f'http://www.omdbapi.com/?apikey={api_key}&s={query}&page={str(page_number)}'

        response = requests.get(url)
        response.raise_for_status()
        movie_data = response.json()
        page_number = int(page_number)+1
        return movie_data,page_number,None
    
    except Exception as e:
        return None,1,str(e)
        
            
def fetchMovieDetails(imdb_id):
    api_key = os.getenv('OMDB_API_KEY')
    
    try:
        if Movie.objects.filter(imdbID=imdb_id).exists():
            movie_data = Movie.objects.get(imdbID=imdb_id)
            return movie_data, True  # Movie is found in the database

        url = f'http://www.omdbapi.com/?apikey={api_key}&i={imdb_id}'
        response = requests.get(url)
        movie_data = response.json()

        if movie_data.get('Response') == 'False': 
            return None, None  
        
        rating_objs = []
        for rate in movie_data.get('Ratings', []):
            r, created = Rating.objects.get_or_create(source=rate['Source'], rating=rate['Value'])
            rating_objs.append(r)

        movie, created = Movie.objects.get_or_create(
            Title=movie_data['Title'],
            Year=movie_data['Year'],
            Rated=movie_data['Rated'],
            Released=movie_data['Released'],
            Runtime=movie_data['Runtime'],
            Genre=movie_data['Genre'],
            Director=movie_data['Director'],
            Writer=movie_data['Writer'],
            Actors=movie_data['Actors'],
            Plot=movie_data['Plot'],
            Language=movie_data['Language'],
            Country=movie_data['Country'],
            Awards=movie_data['Awards'],
            Poster_url=movie_data['Poster'],
            Metascore=movie_data['Metascore'],
            imdbRating=movie_data['imdbRating'],
            imdbVotes=movie_data['imdbVotes'],
            imdbID=movie_data['imdbID'],
            Type=movie_data['Type'],
            BoxOffice=movie_data['BoxOffice'],
        )

        movie.Ratings.set(rating_objs)
        movie.save()

        return movie, False  

    except requests.exceptions.RequestException as e:
        return None, str(e)  


        
        