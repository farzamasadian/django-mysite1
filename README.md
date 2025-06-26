# Django Blog and Newsletter Platform

This is a full-featured web application built with Django. It includes a complete blog engine with posts, comments, and tags, as well as a newsletter subscription feature and a robust user authentication system.

## Features

* **Blog Engine:**
    * Create, edit, and delete blog posts.
    * Posts include title, content, author, published date, and status (draft/published).
    * Support for tagging posts with multiple keywords.
    * A comment system for readers to engage with posts.
    * Views to display lists of posts, individual post details, and posts filtered by tag.

* **Newsletter:**
    * A subscription form for users to sign up for a newsletter.
    * Admin functionality to manage subscribers.
    * (Optional) A system to send out newsletters to all subscribers.

* **User Authentication:**
    * User registration, login, and logout functionality.
    * Password reset via email.
    * User profiles with customizable information.
    * Authentication checks to restrict access to certain pages (e.g., creating posts).

## Tech Stack

* **Backend:** Python, Django
* **Database:** (e.g., PostgreSQL, SQLite, MySQL)
* **Frontend:** HTML, CSS, (e.g., Bootstrap, JavaScript)

## Setup and Installation

To get this project up and running on your local machine for development and testing purposes, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/farzamasadian/django-mysite1.git](https://github.com/farzamasadian/django-mysite1.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd django-mysite1
    ```

3.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure your database:**
    * Update the `DATABASES` setting in `mysite/settings.py` with your database credentials.

6.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

7.  **Create a superuser:**
    * This will be your admin account to manage the site from the Django admin panel.
    ```bash
    python manage.py createsuperuser
    ```

8.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

    The application will be available at `http://127.0.0.1:8000/`. You can access the admin panel at `http://127.0.0.1:8000/admin`.

## Usage

* **Creating a post:**
    1.  Log in to the admin panel.
    2.  Navigate to the "Posts" section and click "Add Post."
    3.  Fill in the required fields and save the post.

* **Managing comments and tags:**
    * Comments and tags can be managed through the Django admin panel.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or create a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.
