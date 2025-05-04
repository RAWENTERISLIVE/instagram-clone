
Built by https://www.blackbox.ai

---

# Instagram Clone

## Project Overview
This project is a simple Instagram-like web application built using Flask and SQLite. It features user registration, login, and password handling with plain text passwords (for demonstration purposes). The application uses a lightweight SQLite database to store user information. It also includes a page to view all registered users and login attempts in a tabular format.

## Installation

To set up the project locally, follow these steps:

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/instagram-clone.git
   cd instagram-clone
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   Make sure you have Flask installed. You can install it using pip:
   ```bash
   pip install Flask
   ```

4. **Create the database:**
   Run the `database.py` script to create the necessary tables:
   ```bash
   python database.py
   ```

## Usage

1. **Run the application:**
   To start the Flask application, run:
   ```bash
   python app.py
   ```

2. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000`.

3. **Features:**
   - User registration (sign up).
   - User login.
   - Secure password handling using SHA-256 hashing.
   - Simple UI for login and registration.

## Features
- **User Authentication:** Allows users to register with a username, email, fullname, and password.
- **Secure Password Storage:** Hashes passwords with SHA-256 for security.
- **Database Management:** Uses SQLite to store user data and ensure data integrity.
- **Flash Messages:** Provides user feedback through flash messages upon registration and login attempts.

## Dependencies
This project requires the following Python packages:
- Flask

You can install them using pip as mentioned in the Installation section.

## Project Structure
```
instagram-clone/
├── app.py                # Main application file
├── database.py           # Script to create database and tables
└── templates/            # Directory containing HTML templates
    ├── index.html       # Login page template
    └── signup.html      # Registration page template
```

- **app.py:** Contains the main application logic, routes for login and registration, and user session management.
- **database.py:** Handles database connection and table creation.
- **templates/:** Stores HTML files used to render the frontend of the application.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
