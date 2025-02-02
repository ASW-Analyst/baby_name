# Baby Name Rating App

As my wife is now pregnant with our first born we started think about what names we liked and more imporantly **ones that we were going to veto**. So what better way than to have an app that will suggest names and we can each individually score them. This repoistory contains all the code for this **flask web app** that suggests a random name to be rated between 0 and 5 stars. Users will login to view the names and have their ratings submitted to a database. This will enable later analysis to find those names we both love.

***

## Repository Structure

```
baby_name/

├── app/
    ├── templates/
        ├── login.html
        └── rate.html
    ├── static/
    ├── __init__.py
    ├── auth.py
    └── main.py
├── data/
    ├── babynames.db
    ├── boysnames2023.xlsx
    └── girlsnames2023.xlsx 
├── models/
    ├── __init__.py
    ├── check_names.py
    ├── check_ratings.py
    ├── check_users.py
    ├── create_database.py
    ├── create_user.py
    ├── database.py
    ├── models.py
    └── populate_names_db.py
├── .env
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── run.py

```
