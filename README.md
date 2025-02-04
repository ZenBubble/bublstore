# bublstore
Full stack project made for a mock website offering various services. Self-hosted backend with a simple html + css frontend

## Features 
### ❤️ = Not yet implemented 
### 💛 = Actively being developed 
### 💚 = Implemented
- ❤️ Basic front end made in html + tailwind. Not really the main focus of this project, but useful to learn.
- 💛 Backend server for saving customer account information + cart/wishlist + reviews, hosted from personal home server (custom django user system + auth). This is the main focus of this project, as I want to explore more of the backend stuff as well as information encryption.
- 💛 Django code base. This is meant for learning more of the python syntax as well as using a new framework.
- ❤️ Automated tests. This is for learning CI/CD and program testing.
- ❤️ Bug reports that save a snapshot of the html at time of bug.
- ❤️ All in one dockerized version to learn docker.
- ❤️ Clippy type mascot that details what each page is and how it was implemented.

## Installation/development
"pip freeze > requirements.txt" to save dependencies

"pip install -r requirements.txt" to install dependencies

## Personal Notes
When making new models (data) or changing existing ones: 
- python manage.py makemigrations store
- python manage.py migrate

When creating new views (pages):
- Create new views in views.py
- Wire them into proper urls in urls.py

For production, run both:
- python manage.py runserver
- python manage.py tailwind start