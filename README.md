# bublstore
Full stack project made for a mock website offering various services. Self-hosted backend with a simple html + css frontend

## Features
- (WIP) Basic front end made in html + css. Not really the main focus of this project, but useful to learn.
- (WIP) Backend server for saving customer account information + cart/wishlist + comments, hosted from personal home server. This is the main focus of this project, as I want to explore more of the backend stuff as well as information encryption.
- (WIP) Django code base. This is meant for learning more of the python syntax as well as using a new framework.
- (WIP) Automated tests. This is for learning CI/CD and program testing.
- (WIP) Bug reports that save a snapshot of the html at time of bug.

## Installation/development
"pip freeze > requirements.txt" to save dependencies

"pip install -r requirements.txt" to install dependencies/virtual environment

Remember to activate virtual environment when working on bublstore

## Personal Notes
When making new models (data) or changing existing ones: 
- python manage.py makemigrations store
- python manage.py migrate

When creating new views (pages):
- Create new views in views.py
- Wire them into proper urls in urls.py