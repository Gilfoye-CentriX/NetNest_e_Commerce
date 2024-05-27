# NetNest E-Commerce

NetNest E-Commerce is a simple online shopping platform built with Flask for the backend and React for the frontend. This project provides basic functionalities for user authentication, product management, and a shopping cart.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- User registration and login
- Product listing and detail view
- Shopping cart management

## Installation

### Prerequisites
- Python 3.8 or higher
- Node.js and npm
- SQLite

### Backend Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/Gilfoye-CentriX/NetNest_e_Commerce.git
    cd NetNest_e_Commerce
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Initialize the database:
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. Run the Flask app:
    ```bash
    flask run
    ```

## Usage
1. Access the application in your browser at `http://localhost:5000`.
2. Register a new user or log in with existing credentials.
3. Browse products, add them to your cart, and view your cart.

### Frontend Setup
1. Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```

2. Install the frontend dependencies:
    ```bash
    npm install
    ```

3. Start the React development server:
    ```bash
    npm start
    ```

## Usage
1. Access the application in your browser at `http://localhost:3000`.
2. Register a new user or log in with existing credentials.
3. Browse products, add them to your cart, and view your cart.

## Project Structure
