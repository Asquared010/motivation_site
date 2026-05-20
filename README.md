# Overview

This project is a motivation tracking web application built using the Django framework. The goal of this software is to strengthen my skills as a software engineer by building a dynamic web application that processes user input, stores data, and displays it through multiple web pages.

The application allows users to submit motivational messages or personal goals through a form. These entries are stored in a database and displayed on a separate page where all saved motivations can be viewed. The system demonstrates full CRUD-style data handling at a basic level (create and read).

To run the program, start the Django development server using:

python manage.py runserver

Then open a browser and navigate to:
http://127.0.0.1:8000/

This will load the home page where users can submit their motivation entries.

The purpose of this software is to practice backend web development, understand how Django processes requests, and learn how web applications store and retrieve data dynamically.

[Software Demo Video](https://www.loom.com/share/34af2e9f63af4de4b7a29c50887398d9)


# Cloud Database

This project uses SQLite as its database, which is the default database system provided by Django for development purposes.

The database stores motivation entries submitted by users. Each entry includes:
- Name (text field)
- Motivation message (text field)
- Timestamp (auto-generated date and time of creation)

The data is managed through Django’s ORM (Object Relational Mapping), which allows interaction with the database using Python code instead of SQL queries directly.

The structure of the database is defined in the Django model file, and migrations are used to automatically create and update the database schema.

# Development Environment

The development environment used for this project includes:

- Visual Studio Code as the code editor
- Python as the programming language
- Django web framework
- SQLite database (built into Django)
- Git and GitHub for version control
- Web browser (Chrome) for testing

Python was used to build backend logic, while HTML and CSS were used for the frontend structure and styling.

# Useful Websites

- https://docs.djangoproject.com/
- https://www.w3schools.com/django/
- https://stackoverflow.com/
- https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django

# Future Work

- Add user authentication so users can log in and track their own motivations
- Improve UI using Bootstrap or a modern frontend framework
- Add ability to delete or edit motivation entries
- Deploy the application online using platforms like Render or Heroku