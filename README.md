📌 Billboard Management System

A Django-based web application designed to manage billboard locations in Harare, Zimbabwe. 
The system tracks the companies renting billboards, their geographical coordinates, and payment status. 
It also integrates with Google Maps to provide directions to billboard locations.

🌟 Features

✅ Manage Billboards – Add, edit, and delete billboard locations.
✅ Track Rentals – Assign billboards to companies and monitor their payment status.
✅ Geographical Coordinates – Add precise latitude and longitude for each billboard.
✅ Google Maps Integration – Click on coordinates to open Google Maps for directions.
✅ Filter & Search – Easily find billboards by location, company, or payment status.
✅ Admin Dashboard – Access a secure /admin panel for managing data.
✅ Online Payments Integration (Coming Soon) – Pay for billboard rentals online.


Tech Stack

Python	Backend programming language
Django	Web framework for backend logic
HTML, CSS	Frontend structure and styling
SQLite	Database for storing billboard information
Heroku	Deployment platform
Google Maps API	Display billboard locations

📂 Project Structure

billboard_manager/
├── billboard_manager/    # Django project settings
│   ├── settings.py       # Configuration file
│   ├── urls.py           # Main URL routes
│   ├── wsgi.py           # WSGI deployment entry point
│   ├── asgi.py           # ASGI deployment entry point
├── billboards/           # Main Django app
│   ├── migrations/       # Database migrations
│   ├── templates/        # HTML templates
│   ├── static/           # Static files (CSS, images)
│   ├── models.py         # Database models
│   ├── views.py          # Business logic
│   ├── urls.py           # App-specific routes
│   ├── forms.py          # Django forms
│   ├── admin.py          # Admin panel configuration
├── manage.py             # Django CLI tool
├── db.sqlite3            # Database file (for local development)
└── requirements.txt      # List of dependencies
