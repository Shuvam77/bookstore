# Bookstore
Bookstore app is a simple online bookstore application, developed as a personal hobby project. It was developed while studying Django for Professionals, written by William S. Vincent.

# Tech Stack
  1. [Python](https://www.python.org/downloads/)
  2. [Django](https://www.djangoproject.com/)
  3. [jQuery](https://jquery.com/)
  4. HTML/CSS
  5. [Bootstrap](https://getbootstrap.com/)
  6. [Docker](https://www.docker.com/)
  7. [PostgreSQL](https://www.postgresql.org/)
  
 # Installation
 **GIT clone from GitHub**
 
 ###### First step is to make a directory.
 ```
 $ mkdir bookstore_project
 $ cd bookstore_project
 ```
 
 ###### Then clone the [Bookstore App Repo](https://github.com/Shuvam77/bookstore) from the GitHub.
 ```
 bookstore_project $ git clone https://github.com/Shuvam77/bookstore.git .
 bookstore_project $ cd bookstore
 ```
 
 ###### Docker Compose
 Build Images and Run Docker Containers
 ```
 bookstore_project/bookstore $ docker build .
 bookstore_project/bookstore $ docker-compose up
 ```
 
 ###### Migrations
 Propogate your models into database schema
 ```
 bookstore_project/bookstore $ docker-compose exec web python manage.py makemigrations
 bookstore_project/bookstore $ docker-compose exec web python manage.py showmigrations
 bookstore_project/bookstore $ docker-compose exec web python manage.py migrate 
 ```
 
 ###### Create Django Superuser
 For super access in application
 ```
 bookstore_project/bookstore $ docker-compose exec web createsuperuser
 
 Username: admin
 Email address: admin@email.com
 Password: sudo@123
 
 URL: http://127.0.0.1:8000/admin/
 ```
 
 ###### Run docker containers
 ```
 bookstore_project/bookstore $ docker-compose up
 or
 bookstore_project/bookstore $ docker-compose up -d (run in background)
 ```
 
 ###### Close docker containers
 ```
 bookstore_project/bookstore $ docker-compose down
 ```
 
 
 
 
