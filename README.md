# Open Movie Database (OMDb) API Data Analysis

Gathers data for Oscar-winning movies using their IMDB ids, saves the information to a CSV file, and answers a few data analysis questions about the movies using JupyterLab.

Google Slides presentation is available at: <https://docs.google.com/presentation/d/1n8Oj3vqyDM5oQEsC2xx6O5cvqLt-SElyxxox1CRYDPM/edit?usp=sharing>

---

## Files Included

* `requirements.txt` - Keeps track of modules used so other developers can run the project.
* `.env.example`- Should be renamed `.env` and filled out with your own API key.
* `oscar_winners.csv` - CSV file containing Movie Titles an dIMDb IDs to be used in analysis.
* `movie_requests.py` - Used to access data and creates a new CSV file named `movies.csv` automatically.
* `movie_analysis` - A Jupyter Notebook containing the analysis.

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

1. What was the runtime for each movie?
2. What movie had the longest runtime?
3. Is there any relationship between the length of the movie (runtime) and the number of awards a movie won?
4. How many awards and nominations did each movie receive?
5. Is there a relationship between the amount of box office earnings a movie had and the amount of total nominations the movie received (total nominations = awards wins + award nominations)?
6. Is there a relationship between box office earnings and movie runtimes?
7. How much did each movie earn at the box office?
8. What is the total count of each genre present in the dataset? (How many times does fantasy, drama, adventure, etc. show up)

---

## Run the app

Clone this repo then `cd omdb-api-data-analysis`.

NOTE: This process assumes you are using `pip` to create an environment and not using Anaconda.

NOTE: In case you installed the requirements using pip previously, you may need to run `pip cache purge` to clear the cache before installing the requirements again. Also `deactivate` then `source env/bin/activate` to make sure you are using the latest/correct environment.

Assuming you have Python3 installed on a MacOS, run these commands (or something similar):

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

👉 Rename the `.env.example` file to `.env` and add your [OMDb API](https://www.omdbapi.com/apikey.aspx):

```bash
cp .env.example .env
```

Then run the script to load the data:

```bash
python movie_requests.py
```

This will read the file `oscar_winners.csv` and gather data on the listed movies from [OMDb](https://www.omdbapi.com/) before creating a new file called `movies.csv` which will be used for the Jupyter Notebook data analysis.

You can then open the Jupyter Notebook using the command line by running:

NOTE: If you had previously opened the notebook, from the 'Run' menu select 'Run All Cells' to clear any previous output.

```bash
jupyter lab movie_analysis.ipynb
```

When done running the app, you can deactivate the virtual environment by running `deactivate`.

---

## Dev Notes

Initial project development process:

1. Create a new repo on GitHub.
2. Clone the repo to my local machine.

```bash
git clone <repo_url>
```

3. `cd` into the repo

```bash
cd <repo_name>
```

4. Create a new virtual environment and activate it.

```bash
python3 -m venv env
source env/bin/activate
```

5. Install the required packages.

```bash
pip install requests
pip install python-dotenv
```

6. Create a `requirements.txt` file so that other developers can install the required packages.

```bash
pip freeze > requirements.txt
```

7. Create a `.gitignore` file to ignore certain files and folders from being tracked by Git.

```bash
# .gitignore
.env
env/
```

8. Create a `.env` file to store environment variables.

```bash
# .env
OMDB_API_KEY=<your_api_key>
```

9. Create a `movie_requests.py` file to make requests to the OMDb API and save the data to a CSV file.

10. Create a `oscar_winners.csv` file to store the movie titles and IMDB IDs to be used in the analysis.

11. Create a `movie_analysis.ipynb` file to analyze the data.

12. Create a `README.md` file to document the project.

13. Push the project to GitHub.

```bash
git add .
git commit -m "Initial commit"
git push origin master
```
