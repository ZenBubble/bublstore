# bublstore
Full stack project made for a mock website offering various services. Self-hosted backend with a simple html + css frontend

## Features 
### ❤️ = Not yet implemented 
### 💛 = Actively being developed 
### 💚 = Implemented
- 💚 Django code base for saving customer account information + cart + reviews. This is meant for learning more of the python syntax as well as using a new framework.
- 💛 Basic front end made in html + tailwind. Not really the main focus of this project, but useful to learn.
- 💛 Custom user authentication and home server hosting. This is the main focus of this project, as I want to explore more of the information encryption and web protocols.
- ❤️ Automated tests using Django tests as well as GitHub actions. This is for learning CI/CD and program testing.
- ❤️ Bug reports that save a snapshot of the html at time of bug.
- ❤️ All in one dockerized version to learn docker.
- ❤️ Clippy type mascot that details what each page is and how it was implemented.

## Installation/development
"pip install -r requirements.txt" to install dependencies, recommended to do in a virtual environment

## Personal Notes
When making new models (data) or changing existing ones: 
- python manage.py makemigrations store
- python manage.py migrate

For production, run both:
- python manage.py runserver
- python manage.py tailwind start