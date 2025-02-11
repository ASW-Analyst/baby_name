# Baby Name Rating App

As my wife is now pregnant with our first born we started think about what names we liked and more imporantly **ones that we were going to veto**. So what better way than to have an app that will suggest names and we can each individually score them. This repoistory contains all the code for this **flask web app** that suggests a random name to be rated between 0 and 5 stars. Users will login to view the names and have their ratings submitted to a database. This will enable later analysis to find those names we both love.

***

## Repository Structure

```
baby_name/

├── app/                        # Flask app
    ├── templates/              # HTML templates for rendering web pages
        ├── login.html          # Login page
        └── rate.html           # Rating page
    ├── static/                 # Hold for CSS and images
    ├── __init__.py             # Initialises the Flask app
    ├── auth.py                 # Logic for authenticating users
    └── main.py                 # Main application logic
├── data/                       # Storage of ONS data and app DB
    ├── babynames.db            # Database of names, users and ratings
    ├── boysnames2023.xlsx      # ONS extract of 2023 boys names
    └── girlsnames2023.xlsx     # ONS extract of 2023 girls names
├── models/                     # Database models and scripts
    ├── __init__.py             # Defines models package
    ├── check_names.py          # Check names loaded into DB correctly
    ├── check_ratings.py        # Check ratings submitted via app correctly
    ├── check_users.py          # Check users created correctly
    ├── create_database.py      # Creates and resets database
    ├── create_user.py          # Creates users
    ├── database.py             # Manages database connection
    ├── models.py               # Defines database tables
    └── populate_names_db.py    # Loads ONS baby names into database
├── .env                        # Environment variables (SECRET_KEY)
├── .gitignore                  # For not tracking specific files
├── LICENSE                     # GPL-3.0 License
├── README.md                   # Documentation for repo
├── requirements.txt            # Python dependencies
└── run.py                      # For running the Flask app

```
## How to Run Locally

### 1. Clone Repository

```sh

git clone https://github.com/ASW-Analyst/baby_name.git
cd baby_name

```
### 2. Set-up Virtual Environment

```sh
python -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Set-up Environment Variables
Create a `.env` file in the root directory:
```
SECRET_KEY=set_secret_key
```

### 5. Create the Database and Load Names
```sh
python -m models.create_database
python -m models.populate_names_db
```

### 6. Create Users
Run the `create_user.py` script to load function for creating a user:
```sh
python -m models.create_user
```
Now you can manually add a test user in an untracked script that sets a username and password:
```sh
python -m manual_add_users
```
### 7. Run the App
```sh
python run.py
```
This will run the app locally making it available at:
* **http://127.0.0.1:5000/**

## Development

- [ ] Solution for running the app online and ensuring DB updated
- [ ] Add styling (i.e. images, CSS etc) to the app pages
- [ ] Experiment with different rating options (drop-down, radio etc.)
- [ ] Reduce names in DB, apply filtering
- [ ] Add name information to DB (i.e. popularity)