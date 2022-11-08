# requests docs: https://requests.readthedocs.io/en/latest/
# dotenv docs: https://github.com/theskumar/python-dotenv

import csv
import os

import requests
from dotenv import load_dotenv

# Load environment variables into the os environment
load_dotenv()

# Get the API key from the environment variable
API_KEY = os.environ.get('OMDB_API_KEY')

# TODO: Clean the data
# TODO: Check for duplicates


def get_movie_data(IMDB):
    """Request data from the OMDB API with the provided IMDB id.

    Args:
        IMDB (string): ID from IMDB to request data for.

    Returns:
        _type_: _description_
    """
    r = requests.get(f'http://www.omdbapi.com/?apikey={API_KEY}&i={IMDB}')
    return r.json()


def create_csv_file(data):
    """Write the data to a CSV file named `movies.csv`.

    Args:
        data (_type_): _description_
    """
    with open('movies.csv', 'w', newline='') as csvfile:
        # Create a sequence of keys to identify the order of values to be written
        fieldnames = ['Title', 'Runtime', 'Genre', 'Awards', 'BoxOffice', 'Rated', 'Director', 'Year', 'Language']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for movie in data:
            # For each value in fieldnames, get the value then write the row
            writer.writerow({field: movie[field] for field in fieldnames})

            # writer.writerow(movie_info)
    print("CSV file movies.csv created")


def main():
    """Get data for each movie in the `oscar_winners.csv` CSV file."""
    with open('oscar_winners.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        movies = []
        for row in reader:
            movies.append(get_movie_data(row['IMDB']))

    # Pass the movies list to the `create_csv_file` function
    create_csv_file(movies)


if __name__ == '__main__':
    main()
