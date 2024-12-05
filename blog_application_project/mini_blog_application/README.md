# Mini Blog Application

This is a simple blog application built with Django. It allows users to view blog posts and interact with the platform. This application is intended to serve as a basic starting point for Django-based blog applications.

## Features

- View blog posts
- Simple page rendering without language configuration
- Basic layout using Django templates

## Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.12 or later
- Django 5.1.3 or later
- A database setup (SQLite is used by default)

## Once the project execute, you can sign in with

http://127.0.0.1:8000/admin/

user: deep
password: deep1983

Then you could do the operations!

## the list of urls are

'post/<int:id>/'
'post/create/'
'post/<int:id>/edit/'
'post/<int:id>/delete/'
'post/<int:id>/add_comment/'
'comment/<int:id>/edit/'
'comment/<int:id>/delete/'
