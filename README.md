# Open Movie Database (OMDb) API Data Analysis

Gathers data on 50 Oscar-winning movies using their IMDB ids, saves the information to a CSV file, and answers a few data analysis questions about the movies using JupyterLab.

---

## Files Included

* `requirements.txt`
* `oscar_winners.csv` - CSV file containing Movie Titles an dIMDb IDs to be used in analysis.
* `movie_requests.py` - Used to access data and creates a new CSV file named `movies.csv` automatically.
* `movie_analysis` - A Jupyter Notebook containing the analysis.
* `.env.example`

---

## Data Fields

* Movie Title (string)
* Runtime (integer)
* Genre (string)
* Award Wins (integer)
* Award Nominations (integer)
* Box Office (integer)
* Rated
* Director
* Released
* Language

---

## Analysis Questions

1. (Graph) What was the runtime for each movie?
2. What movie had the longest runtime?
3. Is there any relationship between the length of the movie (runtime) and the number of awards a movie won?
4. (Graph) How many awards and nominations did each movie receive?
5. Is there a relationship between the amount of box office earnings a movie had and the amount of total nominations the movie received (total nominations = awards wins + award nominations)?
6. Is there a relationship between box office earnings and movie runtimes?
7. (Graph) How much did each movie earn at the box office?
8. (Graph) What is the total count of each genre present in the dataset? (How many times does fantasy, drama, adventure, etc. show up)

---

## Run the app

Clone this repo then `cd omdb-api-data-analysis`.

Assuming you have Python3 installed on a MacOS, run these commands (or something similar):

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

👉 Rename the `.env.example` file to `.env` and edit for your local environment if needed:

```bash
cp .env.example .env
```

Then run the script to load the data:

```bash
python movie_requests.py
```

This will read the file `oscar_winners.csv` and gather data on the listed movies before creating a new file called `movies.csv` which will be used for the Jupyter Notebook data analysis.
