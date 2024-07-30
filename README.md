# Personal Portfolio Website
![2](https://github.com/user-attachments/assets/a25f2389-673d-4143-a2e0-5e104fcde643)

## Description

This repository contains the code for a portfolio website built with Django. It serves as the final project for the NetDevelopment 2024 Adaptive Network Laboratory. The project showcases web development skills and adaptive network configurations using Django. This project aims to create a portfolio website using Django. The website includes sections for displaying personal information, projects, skills, and contact information. It demonstrates the integration of web development and network configurations in a Django environment.

## Features

- Responsive design
- Dynamic content management
- Project showcase with descriptions and images
- Contact form
- Integration with social media profiles

## Installation

To get started with the project, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/portfolio-django.git
    cd portfolio-django
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

## Usage

- Access the website by navigating to `http://127.0.0.1:8000/` in your web browser.
- Log in to the admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials to manage content.

## Configuration

- Update the `settings.py` file with your specific configuration, such as database settings and email configurations.
- Customize the templates in the `templates` directory to match your design preferences.
- Add your personal information, projects, and skills through the admin panel.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Submit a pull request.

## License

This project is open source, you can pull, change, and publish with freely. Element and logo are personal elements of Hilmi Musyafa, you can't usage freely without permission.

## Acknowledgements

- Special thanks to the NetDevelopment 2024 Adaptive Network Laboratory for their guidance and support.
- Inspiration from various online tutorials and open-source projects.
