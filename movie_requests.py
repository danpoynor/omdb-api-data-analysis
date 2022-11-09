"""Request movie data from the OMDB API and write it to a CSV file.

Raises:
    ValueError: Test if API_KEY is None or empty.
    ValueError: Test if IMDB ID is empty.
    ValueError: Test if CSV file is empty.
    csv.Error: Test if CSV file has invalid headers.
    csv.Error: Test if CSV file has no rows.
"""
import csv
import os

import requests
from dotenv import load_dotenv

# Load environment variables into the os environment
load_dotenv()

# Get the API key from the environment variable
API_KEY = os.environ.get('OMDB_API_KEY')

# Potential TODOs:
# Clean the data
# Check for duplicates
# Add a progress bar rather than printing each Title as processed
# Handle more potential errors

# Reference DOCs:
# requests: https://requests.readthedocs.io/en/latest/
# dotenv: https://github.com/theskumar/python-dotenv


def get_movie_data(imdb):
    """Request data from the OMDB API with the provided IMDB id.

    Args:
        imdb (str): ID from IMDB to request data for.

    Returns:
        requests.models.Response: Response object formatted as JSON dictionary.
    """
    # Make sure IMDB id is not empty
    if imdb is None:
        raise ValueError("IMDB ID not set")

    r = requests.get(f'https://www.omdbapi.com/?apikey={API_KEY}&i={imdb}')
    return r.json()


def create_csv_file(data):
    """Write the data to a CSV file named `movies.csv`.

    Args:
        data (list): A list of dictionaries containing data to write to the CSV file.
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
    print(f'CSV file movies.csv created and containing {len(data)} movies.')
    print('-'*79)


def main():
    """Get data for each movie in the `oscar_winners.csv` CSV file."""

    # Throw an error if API_KEY name is not defined
    try:
        api_key_test = API_KEY
    except NameError:
        print("API_KEY is not defined.")

    # Test API_KEY value is not None or empty
    api_key_value_test = API_KEY
    if api_key_value_test is None:
        raise ValueError("API_KEY is None.")
    elif api_key_value_test == "":
        raise ValueError("API_KEY is empty.")

    # Assume all's well and continue
    with open('oscar_winners.csv') as csv_file:
        fieldnames = ['Movie', 'IMDB']
        reader = csv.DictReader(csv_file)
        headers = reader.fieldnames

        # Sanity check to make sure the correct headers are present
        if reader.fieldnames is None or len(set(fieldnames).intersection(set(headers))) == 0:
            raise csv.Error("CSV Error: Invalid headers: %s" % str(headers))

        # Check the number of rows is not 0
        elif reader.line_num == 0:
            raise csv.Error("CSV Error: No rows in CSV file")

        # Else assume the file is valid and continue
        else:
            # Show row count as file is processed
            # NOTE: If csv file is large, might want to avoid opening it twice
            # REF: https://stackoverflow.com/questions/2890549/number-of-lines-in-csv-dictreader/2891061#65006592
            # -1 to skip header
            total_rows = sum(1 for _ in open('oscar_winners.csv'))
            print('-'*79)
            print(f'Processing {total_rows - 1} rows from oscar_winners.csv')
            print('-'*79)

            movies = []
            for row in reader:
                print(f"Processing data for tile: {row['Movie']}")
                movies.append(get_movie_data(row['IMDB']))

            print('-'*79)
            print('Data retrieved successfully.')
            print('-'*79)

            # Pass the movies list to the `create_csv_file` function
            create_csv_file(movies)


if __name__ == '__main__':
    main()
