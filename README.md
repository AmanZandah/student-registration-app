# Student Registration App

A full-stack web application that registers students and displays them in a live list. Built with **Flask** and **MySQL**, with deployment automated via **Jenkins**.

> This Flask application is the reusable core of a DevOps internship portfolio — the same app is later deployed on AWS Elastic Beanstalk, containerized with Docker/ECR, and used as the web tier in a Terraform 3-tier architecture.

---

## Features

- Student registration form with both client-side and server-side validation
- Persistent storage in MySQL — data survives application restarts
- Live, auto-updating list of registered students
- Database credentials kept out of source code via environment variables
- SQL-injection-safe parameterized queries

## Tech Stack

- **Backend:** Python, Flask
- **Database:** MySQL 8.0
- **Frontend:** HTML, CSS (rendered with Jinja2 templates)
- **CI/CD:** Jenkins
- **Version control:** Git & GitHub

## Architecture

```
Browser (HTML form)
   --> Flask routes (app.py)
        --> MySQL (student_db.students)
```

The browser submits the form to Flask's `/register` route. Flask validates the input and inserts it into MySQL using a parameterized query. The home route (`/`) reads every student back from the database and renders the list with Jinja2.

## Project Structure

```
student-registration-app/
├── app.py              # Flask application + routes
├── requirements.txt    # Python dependencies
├── schema.sql          # Database + table definition
├── .env.example        # Template for required environment variables
├── .gitignore
├── templates/
│   └── index.html      # Registration form + student list
└── static/
    └── style.css       # Styling
```

> `.env` (real credentials) and `venv/` are intentionally **not** committed — see [Security](#security).

## Setup Instructions

**Prerequisites:** Python 3.x, MySQL 8.0, Git.

1. **Clone the repository**
   ```bash
   git clone https://github.com/AmanZandah/student-registration-app.git
   cd student-registration-app
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/Scripts/activate      # Windows (Git Bash)
   # source venv/bin/activate        # macOS / Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create the database and table**
   ```bash
   mysql -u root -p < schema.sql
   ```

5. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and set `DB_PASSWORD` to your MySQL root password.

6. **Run the app**
   ```bash
   python app.py
   ```
   Open http://localhost:5000 in your browser.

## Security

- Database credentials load from a `.env` file that is excluded from version control via `.gitignore`, so secrets never reach GitHub.
- All SQL uses parameterized queries (`%s` placeholders) to prevent SQL injection.
- `.env.example` documents the required variables without exposing real values.

## CI/CD

*(In progress)* A Jenkins pipeline automates pulling the latest code from GitHub, installing dependencies, and deploying the application. Pipeline definition lives in the `Jenkinsfile`.

## Challenges Faced

- Installing MySQL on Windows and connecting Flask to it (authentication method and connector setup).
- Keeping credentials out of source code by moving them into environment variables.
- Learning the Git workflow — running commands from the correct folder, fixing remotes, and ensuring secrets are never committed.

## Future Improvements

- Add update and delete operations for full CRUD functionality.
- Add search, edit, and pagination for the student list.
- Containerize the app with Docker and deploy on AWS (Elastic Beanstalk or EC2 + RDS).
- Add automated tests that run inside the CI pipeline.
