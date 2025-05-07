
# Tweekly App

This is a social networking platform built using Django, designed to allow users to share posts, interact with each other, and manage their profile information. The app includes features similar to a Facebook-style feed, where users can upload images, post text, and engage with other users via likes, comments, and shares.

## Features

- **User Profile**: Users can upload a profile photo and manage their personal information.
- **Posts**: Users can create text posts, upload images, and view posts made by others.
- **Post Interactions**: Users can like, comment, and share posts. (Note: Like, Comment, and Share buttons are placeholder functionality that can be expanded.)
- **Edit/Delete Posts**: Users can edit or delete their own posts.
- **Responsive Design**: The layout is designed to be mobile-friendly and looks great on various screen sizes.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Tailwind CSS for styling)
- **Database**: PostgreSQL
- **Image Handling**: Django ImageField for profile and post images

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/tweek-app.git
cd tweek-app
````

### 2. Set Up a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Database

Make sure you have PostgreSQL installed and set up. In the `settings.py` file, configure the database settings as per your environment:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tweek_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Apply Migrations

Run the following command to set up the database tables:

```bash
python manage.py migrate
```

### 6. Create a Superuser

Create a superuser to access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to create the superuser.

### 7. Run the Development Server

Start the server to test the application locally:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your web browser.

## Folder Structure

```
tweek-app/
│
├── tweeks/                 # Main app for user posts
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates for the app
│   ├── static/             # Static files (CSS, JS, Images)
│   └── models.py           # Models for user posts and profile
│
├── users/                  # User-related features (authentication, profile)
│   └── models.py           # Custom user model
│
├── media/                  # Folder where uploaded images are stored
│
├── manage.py               # Django project management script
└── settings.py             # Django settings
```

## Template Overview

This project includes the following key templates:

### **Base Template (`base.html`)**

Contains the structure of the app, including common elements like the header, footer, and navigation.

### **Post Feed (`tweek_app.html`)**

Displays the list of posts in the user's feed. Each post includes the user's profile picture, post content, and action buttons like edit, delete, like, comment, and share.

### **User Profile (`user_profile.html`)**

Allows users to manage their profile photo and other personal details.

## Contributing

We welcome contributions to enhance the functionality of the Tweek app! Here’s how you can contribute:

1. Fork this repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request with a detailed description of your changes.

## License

This project is license-free, so you can use it for your own needs. But if you find it well, then you can provide a star in this repo also.

## Acknowledgments

* This app uses [Django](https://www.djangoproject.com/) for the backend.
* The frontend is styled with [Tailwind CSS](https://tailwindcss.com/).
* Icon images used in buttons (like, comment, share) are from [Icon8](https://icons8.com/).


Feel free to customise and extend this README as needed for your project. It provides a basic setup and explanation of the app, and you can add more sections for additional functionality or features as your project evolves.


### Explanation of Sections:

- **Features**: Lists the core functionality of the app.
- **Tech Stack**: Details the technologies used for building the app.
- **Installation**: Step-by-step guide to getting the app up and running on a local machine.
- **Folder Structure**: Provides an overview of how the project is organised.
- **Template Overview**: Describes the important templates used in the project (like the base template and post feed).
- **Contributing**: Instructions for contributing to the project.
- **License**: Information about the license under which the project is distributed (MIT License).
- **Acknowledgements**: Gives credit to tools, libraries, or frameworks used in the project.

This `README.md` should provide clear instructions for setting up and contributing to your Tweekly app and give insight into the project's structure and features.
