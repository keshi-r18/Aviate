# Django Applicant Tracking System (ATS) API

This project is a simple Applicant Tracking System (ATS) built with the Django Rest Framework. It provides a set of API endpoints to manage candidates and includes a powerful, relevance-based search functionality.

This solution was created to fulfill an assignment requiring a deep understanding of the Django Rest Framework, with a focus on leveraging the ORM for efficient, database-driven filtering and sorting.

## Features

- **Full CRUD Operations**: Create, Read, Update, and Delete candidates.
- **Advanced Search**: Search for candidates by name. The search supports partial matches across multiple words.
- **Relevance-Based Sorting**: Search results are automatically sorted by relevance. Relevance is defined as the number of words from the search query that are found in a candidate's name.
- **Efficient ORM Usage**: All filtering and sorting logic is executed directly by the database using a single, optimized query for maximum performance, as required by the assignment.
- **Browsable API**: The entire API can be explored and tested directly in the web browser, thanks to Django Rest Framework's browsable API.

## Requirements

- Python 3.8+
- Django
- Django Rest Framework
- Django-filter

## Setup and Installation

Follow these steps to get the project up and running on your local machine.

1.  **Clone the Repository**
    ```bash
    git clone <your-repository-url>
    cd <repository-directory>
    ```

2.  **Create and Activate a Virtual Environment**
    ```bash
    # For Windows
    python -m venv .venv
    .venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install Dependencies**
    A `requirements.txt` file can be created, but for this project, you can install the packages directly:
    ```bash
    pip install django djangorestframework django-filter
    ```

4.  **Apply Database Migrations**
    This will create the `Candidate` table in the SQLite database.
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Run the Development Server**
    ```bash
    python manage.py runserver
    ```
    The API will now be available at `http://127.0.0.1:8000/api/`.

## API Endpoints

All endpoints are located under the `/api/` path.

### Candidate Management

-   **Endpoint**: `/api/candidates/`
-   **Methods**:
    -   `GET`: Lists all candidates. This is also where you perform searches.
    -   `POST`: Creates a new candidate.
-   **Endpoint**: `/api/candidates/{id}/`
-   **Methods**:
    -   `GET`: Retrieves a single candidate by their ID.
    -   `PUT` / `PATCH`: Updates a candidate's information.
    -   `DELETE`: Deletes a candidate.

### How to Search

The relevance-based search is integrated directly into the candidate list endpoint.

1.  Navigate to `http://127.0.0.1:8000/api/candidates/` in your browser.
2.  Click the **"Filters"** button at the top of the page.
3.  A form will appear. Enter your search query (e.g., "Ajay Kumar") into the **"Search by Name"** field.
4.  Click the "Filter" button to see the results, which will be sorted by relevance.
