######## DJANGO


####### SOME TERMS
# Project is the site
# Apps are the additions you add to the project i.e : store
# All projects are created in a virtual environment when using Django

###### Create a virtual environment
% python3 -m venv ./venv 

# This creates a venv directory

###### Activate the environment
% source ./venv/bin/activate

# Once activated it will use the version of python that activated 
# the environment (dont need to use python3 it is set and you can 
# change the interpreter on Vscode: as long as in root folder)

% python --version                                                                   !2946
Python 3.8.5
(venv) 

####### De-activate it
% deactivate
  
% python --version                                                                   !2948
Python 2.7.16

###### See what packages are installed in the "ENV"
% source ./venv/bin/activate
% pip freeze

# No packages  
% pip freeze                                                                         !2950
(venv)

###### Installing DJANGO
% pip install DJANGO

# Check to see what installed
% pip freeze
% django-admin help (all commands available)

###### Start project in env and root
% django-admin startproject btre .
# This creates a lot of files

# # To see what manage.py can do: run this
% python manage.py help

# Type 'manage.py help <subcommand>' for help on a specific subcommand.

###### Initialise git
% git init 

# Use gitignore.io 
# Add django and it gives us a good default list to ignore
*.log
*.pot
*.pyc
__pycache__/
local_settings.py
db.sqlite3
db.sqlite3-journal
media
venv

% git add . && git commit -m 'Initial commit'

###### Start DJANGO http:// server
% python manage.py runserver

August 07, 2020 - 18:42:35
Django version 3.1, using settings 'btre.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

###### 1st APP [PAGES]
% python manage.py startapp pages

# This creates a pages folder with:
# migrations: folder for migration deactivate
# admin: if you want to show stuff in the admin area
# apps.py: shows the class of the config
# models: creates the modelstests: for tests
# views: to create methods

##### Add the app that we created to the settings file
# Add "pages.apps.PagesConfig" under INSTALLED_APPS
# Add whatever is in apps.py

# Had to add
import os
# to the settings.py file to stop the errors

# To install a helper : 
% pip install autopep8

###### NOW: create the urls.py file & add:
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index')
]

###### Now: create the method/function in views.py file & add:
from djang0.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello World</h1>')

###### Now: Add the path to the main urls.py file
from django.urls import path

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
]

###### Add the include module to the list in views.py
from django.urls import path, include

###### Rendering templates and not:
# return HttpResponse('<h1>Hello World</h1>')

1. Tell Django where to look for templates in settings.py
        'DIRS': [os.path.join(BASE_DIR, 'templates')],

    In the root create the templates directory to save all template files
    In the templates folder create the pages folder
    Create an about.html and home.html file in the pages folder

    In the views file add the method

# In the url.py file    
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about')
]

###### STATIC files # Static files (CSS, JavaScript, Images)
# Make sure to get static files and all static resources loaded its set
# properly: In the settings file add:

STATIC_ROOT= os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'btre/static')
]

# using paython manage.py help, you can see that statis files are collected
% python manage.pt help
[staticfiles]
    collectstatic
    findstatic
    runserver

###### TEST collectstatic
% python manage.py collectstatic
164 static files copied to '/Users/craigleppan/Local/Local-Dev/TUTS/Python/Traversy-Django/btre_project/static'.

## Adds a "static" folder to the btre folder automatically when we run this command
# Add this to .gitignore to stop it being uploaded
/static

###### PARTIALS
# We can unclutter the base.html and remove lots of content to PARTIALS
# Create a folder called partials in the templates folder
# create _footer.html, navbar.html and topbar.html and cut all these
# sections to into these files.
# Refer to these from base.html

###### Create dynamic nav actives
            <ul class="navbar-nav">
                <li 
                    {% if '/' == request.path %}
                        class="nav-item active mr-3"
                    {% else %}
                        class="nav-item mr-3"
                    {% endif %}
                >
                    <a class="nav-link" href="{% url 'index' %}">Home</a>
                </li>
                <li 
                    {% if 'about' == request.path %}
                        class="nav-item active mr-3"
                    {% else %}
                        class="nav-item mr-3"
                    {% endif %}
                >

###### Create the other pages
% python manage.py startapp listings
% python manage.py startapp realtors
# Create a folder for listing and realtors under the templates folder

# In the Django created listings folder we need to create a url.py
# Everything in here will be /listings
urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing')
    path('search', views.search, name='listing')
]
# Now we need to register this in the root url.py file
urlpatterns = [
    path('', include('pages.urls')), # home page
    path('listing/', include('listings.urls')), # listings page
    path('admin/', admin.site.urls)
]

# Now register Listings and Realtors in the settings file in the 
# installed apps sections: Realtors has no views, only a models
INSTALLED_APPS = [
    'pages.apps.PagesConfig',
    'listings.apps.ListingsConfig',
    'realtors.apps.RealtorsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Now create view methods for listings in views.py (index, listing and search)
from django.shortcuts import render

# Create your views here.

# main listings page (index)
def index(request):
    return render(request, 'listings/listings.html')

# view of a listing
def listing(request):
    return render(request, 'listings/listing.html')

# The search view
def search(request):
    return render(request, 'listings/search.html')


###### Add to the pages (html) in templates folder
###### Add the base html to new files

###### POSTGRES DJANGO SETUP
# from term 'psql postgres'
> CREATE DATABASE btredb OWNER craigleppan;
> \PASSWORD 'new';

# Schema model/planning
=== Listings
id: int
realtor: int (Foreign key [realtor])
title: string
address: string
city: string
zipcode: string
description: text
price: int
bedrooms: int
bathrooms: int
garage: int 
sqft: int 
is_published: bool (true)
lot_size: float 
list_size: float
list_date: date
photo_main: string 
photo_1: string
photo_2: string 
photo_3: string 
photo_4: string 
photo_5: string 
photo_6: string 

=== Realtors
id: int
name: string 
photo: string
description: text
email: string
phone: string 
is_mvp: bool (default [0])
hire_date: date

=== Contact (inquiries sent in)
id: int 
user_id: int
listing: int 
listing_id: int 
name: string 
email: string 
phone: string 
message: text 
contact_date: date

###### Creating models in Django
https://docs.djangoproject.com/en/3.1/ref/models/fields/
# listings model: go to listings/model
from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title

# Realtors model
from django.db import models
from datetime import datetime

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name 

# When using ImageField need to install Pillow
% pip install Pillow

###### Running migrations
% python manage.py makemigrations
# Created both migration 0001 for both Realtor and Listing
% python manage.py makemigrations                                                        !3011
Migrations for 'realtors':
  realtors/migrations/0001_initial.py
    - Create model Realtor
Migrations for 'listings':
  listings/migrations/0001_initial.py
    - Create model Listing

## Option to see SQL used to create the migration to postgres
% python manage.py sqlmigrate listings 0001
BEGIN;
--
-- Create model Listing
--
CREATE TABLE "listings_listing" ("id" serial NOT NULL PRIMARY KEY, "title" varchar(200) NOT NULL, "address" varchar(200) NOT NULL, "city" varchar(100) NOT NULL, "state" varchar(100) NOT NULL, "zipcode" varchar(20) NOT NULL, "description" text NOT NULL, "price" integer NOT NULL, "bedrooms" integer NOT NULL, "bathrooms" numeric(2, 1) NOT NULL, "garage" integer NOT NULL, "sqft" integer NOT NULL, "lot_size" numeric(5, 1) NOT NULL, "photo_main" varchar(100) NOT NULL, "photo_1" varchar(100) NOT NULL, "photo_2" varchar(100) NOT NULL, "photo_3" varchar(100) NOT NULL, "photo_4" varchar(100) NOT NULL, "photo_5" varchar(100) NOT NULL, "photo_6" varchar(100) NOT NULL, "is_published" boolean NOT NULL, "list_date" timestamp with time zone NOT NULL, "realtor_id" integer NOT NULL);
ALTER TABLE "listings_listing" ADD CONSTRAINT "listings_listing_realtor_id_90583529_fk_realtors_realtor_id" FOREIGN KEY ("realtor_id") REFERENCES "realtors_realtor" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "listings_listing_realtor_id_90583529" ON "listings_listing" ("realtor_id");
COMMIT;

###### MIGRATE the made model migration files to postgres
% python manage.py migrate 
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, listings, realtors, sessions
Running migrations:
  Applying realtors.0001_initial... OK
  Applying listings.0001_initial... OK

###### Admin area !!!!
localhost:8000/admin
% python manage.py help
% python manage.py createsuperuser ( used craigleppan and basic)

###### Registering models for admin use
# Under listings/admin.py
from .models import Listing
admin.site.register(Listing)

# for the Realtors add this to admin.py
from .models import Realtor
admin.site.register(Realtor)

###### Django media folder definition
# Media folder settings where media stored on HDD
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# In the url.py file (main one) add:
# after the urlpatterns = [...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

###### CHANGING ADMIN site
# In the templates folder create a folder called admin
# admin then file : base_site.html

# Changing the listings page : what is shown
# add to the admin.py a class
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'zipcode', 'price')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)

# Change the Realtors admin page: at admin.py in realtors folder
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)

##### Methods to view from model
# Listings, to enable listing the model in the views we need to call from the 
# listing table and place in the view.pl def

# 1st we add the ability to call models in the views.py file
from .models import Listing

# Old:
def index(request):
    return render(request, 'listings/listings.html')

# 2nd New: 
def index(request):

    listings = Listing.objects.all()

    context = { 'listings': listings }

    return render(request, 'listings/listings.html', context)

# 3rd, now in the html template loop through the listings is they exist
# use {{ listings.xxx }}

###### Humanise the price with a comma with an app called Humanise
# Add in the settings file: INSTALLED_APPS
    'django.contrib.humanize',

# to use humanize we need to load it in the file
{% load humanize %} see google

###### PAGINATION
# In the views.py file (listings).
# Create your views here.
# main listings page (index)
def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = { 'listings': paged_listings }

    return render(request, 'listings/listings.html', context)

# In the listings.html file add the paginator at the bottom

{% if listings.has_other_pages %}

    <ul class="pagination">
        {% if listings.has_previous %}
            <li class="page-item">
                <a href="?page={{listings.previous_page_number}}" class="page-link">&laquo;
                </a>
            </li>
        {% else %}
        <li class="page-item disabled">
            <a class="page-link">&laquo;</a>
        </li>
        {% endif %}
        {% for i in listings.paginator.page_range %}
            {% if listings.number == i %}
                <li class="page-item active">
                    <a class="page-link">{{i}}</a>
                </li>
            {% else %}
                <li class="page-item">
                    <a href="?page={{i}}" class="page-link">{{i}}</a>
                </li>
            {% endif %}
        {% endfor %}
        {% if listings.has_next %}
        <li class="page-item">
            <a href="?page={{listings.next_page_number}}" class="page-link">&raquo;
            </a>
        </li>
        {% else %}
        <li class="page-item disabled">
            <a class="page-link">&raquo;</a>
        </li>
        {% endif %}
    </ul>

{% endif %}

###### Accounts and creating Accounts
% python manage.py startapp accounts

# Add the app to settings
INSTALLED_APPS = [
    'accounts.apps.AccountsConfig',

# Django already has a user system in place so we dont need to create this
# We just use the user table in place, through this app: SEE auth.user table for
# fields

SELECT 
   table_name, 
   column_name, 
   data_type 
FROM 
   information_schema.columns
WHERE 
   table_name = 'auth_user';

id, password, last_login, is_superuser, username, first_name, last_name, email, 
is_staff, is_active, date_joined

# We need to create templates for the table so we can administer the table

###### Create admin templates
# Under templates create 
login.hlml, register.html and dashboard.html

# Create the urls.py file in the app 'accounts'
from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard')
]

# Now in the views.py create the views methods
from django.shortcuts import render, redirect

# Create your views here.

def register(request):
    return render(request, 'accounts/register.html')


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index') # add import of redirect


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


###### Add and  test the routes to see if they are working
# In the btre/urls.py file add the accounts app to routes

urlpatterns = [
    path('', include('pages.urls')), # home page
    path('listings/', include('listings.urls')), # listings page
    path('accounts/', include('accounts.urls')), # accounts page
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

localhost:8000/accounts/login
# fix the links on main pages to go to these pages
<a class="nav-link" href="{% url 'register' %}">
<a class="nav-link" href="{% url 'login' %}">

# Add conditionals to show links active
                <li
                    {% if 'login' in request.path %}
                        class="nav-item active mr-3"
                    {% else %}
                        class="nav-item mr-3"
                    {% endif %}
                >
                    <a class="nav-link" href="{% url 'login' %}">
                        <i class="fas fa-sign-in-alt"></i>

                        Login</a>
                </li>

# Add the base.html wrapper to the html files created
{% extends 'base.html' %}
{% load humanize %}

{% block content %}
html goes here
{% endblock %}

###### The register form in register.html needs to submit to register
# So change the action in form to go to the register method
<form action="{%  url 'register' %}" method="POST">
# Same for login
<form action="{% url 'login' %}" method="POST">

###### When we have a form and we are submitting a POST request
# we need to add a csrf token. This prevents cross site forgery.
# Ties the form to the current sessions
# Easily done in Django: just after the action add:
{% csrf_token %}

# In the apps view.py file we need to descriminate between post and get
# In the accounts view.py file
def register(request):
    if request.method == 'POST':
        print('SUBMITTED REG')
        return redirect('register')
    else: 
        return render(request, 'accounts/register.html')
# Check in the logs if you are getting the : SUBMITTED REG

###### Messaging/Alerts [Flash messages]
# Django comes with a messaging app by default, just needs configuration
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# Make a partial alert that works with bootstrap
{% if messages %}

    {% for message in messages %}

        <div id="message" class="container">
            <div class="alert alert-{{ message.tags }} alert-dismissable text-center" role="alert">
                <button type="button" class="close" data-dismiss="alert">
                    <span aria-hidden="true">&times;</span>
                </button>
                <strong>
                    {% if message.level == DEFAULT_MESSAGE_LEVELS.ERROR %}
                        Error: 
                    {% else %}
                        {{ message.tags|title }}
                    {% endif %}
                </strong>
                {{ message }}
            </div>
        </div>

    {% endfor %}

{% endif %}

###### Create some javascrpt to remove the error after a while
# under btre/js/main.js
setTimeout(function() {
  $('#message').fadeOut('slow');
}, 3000);

# AFTER ADDING to main.js we need to run:
% python manage.py collectstatic

###### User registration 
# import the model from django
from django.contrib.auth.models import User

# Aslo when authenticating we need to import from contrib auth
from django.contrib import messages, auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        # Register the user after successful form app
        # test message
        # messages.error(request, 'Testing error message')
        # return redirect('register')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is in use')
                    return redirect('register')
                else:
                    # Looks good so create the user
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # login after registration can log in but prefer to register then login normally
                    # auth.login(request, user)
                    # messages.success(request, 'You are now registered and logged in')
                    # return redirect('register')

                    # Alternative prefered is:
                    user.save();
                    messages.success(request, 'You are now registered and can login')
                    return redirect('login')

###### Login
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else: 
        return render(request, 'accounts/login.html')

###### Customizing the titles in the tab
# Best done in the base.html
<title>BTRE {% block title %}{% endblock %}</title>

# in index below humanize
{% block title %}| Welcome {% endblock %}

##### Manage Contacts and inquiries
# Create the app
% python manage.py startapp contacts

# in models.py create the table schema
# 1st bring in datetime at top
from django.db import models
from datetime import datetime

class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.name

# Create a migration file
% python manage.py makemigrations contacts

# WONT RUN AS THE APP is not registered in settings so register it
INSTALLED_APPS = [
    'contacts.apps.ContactsConfig',

% python manage.py makemigrations contacts
Migrations for 'contacts':
  contacts/migrations/0001_initial.py
    - Create model Contact

# NOW migrate the file: or whats no migrated
% python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contacts, contenttypes, listings, realtors, sessions
Running migrations:
  Applying contacts.0001_initial... OK

# Table migrated and ready: you can see above all were up except contacts so it ran it
# Like: rake db migrate

###### Registering contacts in the admin area so we can edit 
# Register your models here to see it in /admin
from .models import Contact

# add this to customise
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)

##### Get the contact to be submitted through model in listing.html
# make the model's action correct with POST to correct url
# Secure with csrf token
            <div class="modal-body">
                <form action="{% url 'contact' %}" method="POST">
                {% csrf_token %}

# NB: if a user is logged in then send the details else set user_id to 0
            <div class="modal-body">
                <form action="{% url 'contact' %}" method="POST">
                    {% csrf_token %}
                    {% if user.is_authenticated %}
                        <input type="hidden" name="user_id" value="{{ user.id }}" >
                        {% else %}
                        <input type="hidden" name="user_id" value="0" >
                    {% endif %}
                    <div class="form-group">

# Make a contact path in contact/urls.pyfrom django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact, name='contact')
]

# include it in the main urls.py
urlpatterns = [
    path('', include('pages.urls')), # home page
    path('listings/', include('listings.urls')), # listings page
    path('accounts/', include('accounts.urls')), # accounts page
    path('contacts/', include('contacts.urls')), # accounts page
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Create the view.py file
from django.shortcuts import render, redirect
# import ther standard messages
from django.contrib import messages

# import the contact model
from .models import Contact

# Create your views here.
def contact(request):
    # return
    if request.method == 'POST':
        # print('HELLO')
        # return
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id )
        contact.save()

        messages.success(request, 'Your inquiry is lodged, a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)

# to enable messages<!-- Alerts -->
{% include 'partials/_alerts.html' %}






