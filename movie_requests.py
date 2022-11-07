# Install the Python Requests library:
# `pip install requests`

import requests
import csv
import os

# Get the API key from the environment variable
API_KEY = os.environ.get('OMDB_API_KEY')

# Create a function to request data from the OMDb API for
# each movie in the CSV file using their IMDB ids.

# Save the returned data to a new CSV file named movies.csv. It should include:
# Movie Title (string)
# Runtime (integer)
# Genre (string)
# Award Wins (integer)
# Award Nominations (integer)
# Box Office (integer)
# Rated
# Director
# Released
# Language
