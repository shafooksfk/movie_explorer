An IMDB Clone Application Using Django and OMDB API

Technologies Used: Django, Jinja

How to run the application:
 - Clone the git repo after creating a fork.
 - Make sure python is intalled in your system
 - `pip install -r requirements.txt` run this command to install the required packages for the application.
 - `python manage.py migrate` run the following to setup the database schema.
 - From the website of OMBD `https://www.omdbapi.com/ ` generate API Key
   - Generated API Key will shared through mail
   - Copy the API KEY and store in `.env` file in the root folder of the django project.
   - format  `OMDB_API_KEY=[YOUR_API_KEY]` 
 -` python manage.py runserver` run this command to see the application running.🎉🎊

