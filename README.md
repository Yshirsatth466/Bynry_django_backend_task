# Gas Utility Management System

## Overview  
This project is a Django-based web application designed for a gas utility company to manage customer service requests. The system streamlines customer interactions by allowing users to submit service requests, track their statuses, and view account information. It also provides an admin dashboard for customer support representatives to manage and resolve requests efficiently.  

## Features  

### Customer Features  
- **User Registration and Authentication**  
  - Customers can register, log in, and log out securely.  

- **Submit Service Requests**  
  - Customers can submit service requests online, specifying the type of service and additional details.  

- **Track Requests**  
  - View the list of submitted service requests and their current statuses (e.g., Pending, In Progress, Resolved).  

- **Request Details**  
  - View detailed information about individual requests.  

### Admin Features  
- **Dashboard**  
  - Admins can view all submitted requests and manage their statuses.  

## Technologies Used  
- **Backend**: Django 4.x  
- **Frontend**: HTML5, CSS3, Bootstrap  
- **Database**: SQLite (default, can be replaced with PostgreSQL or MySQL)  
- **Authentication**: Django’s built-in authentication system  

## Project Structure  

```plaintext
gas_utility/
├── accounts/                 # Manages user authentication
│   ├── templates/accounts/   # HTML templates for user login and registration
├── requests/                 # Handles customer service requests
│   ├── templates/requests/   # HTML templates for request management
├── dashboard/                # Admin dashboard for request management
│   ├── templates/dashboard/  # HTML template for the admin dashboard
├── gas_utility/              # Project settings and URLs
└── manage.py                 # Django's command-line utility
