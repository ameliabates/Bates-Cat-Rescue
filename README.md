# Bates Cat Rescue Management System

## Overview

The Bates Cat Rescue Management System is a web-based platform designed to facilitate the management of cat adoption records, display available cats, and provide an administrative tool for adding, removing, and updating cat information. The system integrates a database, server-side API, and frontend interface.

## Features

-   **Admin Tool:** Allows administrators to add, remove, and update cat records.
    
-   **Database Integration:** Uses SQLite to store and manage cat data.
    
-   **Web Interface:** Displays available cats with relevant details.
    
-   **Server API:** Fetches cat data from the database for the frontend.
    
-   **Static File Hosting:** Serves frontend assets including HTML, CSS, and JavaScript.
   
## Installation & Setup

### Prerequisites

Ensure you have the following installed:

-   Python (for admin tool and database management)
    
-   Node.js (for server API)
    
-   SQLite (for database management)
    

### Backend Setup

1.  Install dependencies:
    
    ```
    npm install express csv-parser
    ```
    
2.  Run the server:
    
    ```
    node server.js
    ```
    

### Database Setup

1.  Initialize the database by running:
    
    ```
    python admin.py
    ```
    
2.  Follow the prompts to add initial cat data.
    

### Frontend Setup

1.  Open `index.html` in a browser.
    
2.  Ensure the server is running to fetch the latest cat data.
    

## Usage

-   **To Add a Cat:** Run `admin.py` and select the appropriate option.
    
-   **To Remove a Cat:** Use the admin tool and specify the cat's name.
    
-   **To View Available Cats:** Open the `available_cats.html` page.
    

## API Endpoints

-   `GET /cats`: Fetches all available cats from the database.
    

## Technologies Used

-   **Python & SQLite** (Database management)
    
-   **Node.js & Express** (Server API)
    
-   **HTML, CSS, JavaScript** (Frontend display)
