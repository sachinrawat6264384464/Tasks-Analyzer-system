📘 Backend — Smart Task Analyzer (Django REST API)
🚀 Overview

This is the backend of the Smart Task Analyzer application.
It provides:

User registration & login

Task creation per user

Smart task analysis API

Priority scoring algorithm

Task suggestion engine

REST APIs for frontend (React)

⚙️ Tech Stack

Python 3.8+

Django 4+

Django REST Framework

SQLite Database

📁 Project Structure
backend/
│── manage.py
│── task_analyzer/
│── tasks/
│   │── models.py
│   │── serializers.py
│   │── views.py
│   │── scoring.py
│   │── urls.py
│   │── tests.py
│── users/ (for registration/login)

🔧 Installation & Setup
1. Install dependencies
pip install -r requirements.txt

2. Run migrations
python manage.py makemigrations
python manage.py migrate

3. Start server
python manage.py runserver


Backend will run on:
👉 http://localhost:8000

🔐 Authentication Endpoints
POST /api/users/register/

Registers a new user.

POST /api/users/login/

Returns a token for login.

📝 Task Endpoints
POST /api/tasks/create/

Create a task (authenticated user only)

GET /api/tasks/list/

List all tasks of a logged-in user

POST /api/tasks/analyze/

Input: list of tasks
Output: priority score + explanation + sorted tasks

GET /api/tasks/suggest/

Returns top 3 task recommendations

🧠 Priority Scoring Algorithm

Algorithm calculates priority using four core factors:

1. Urgency
urgency_score = 10 - days_left

2. Importance
importance_score = importance * 2

3. Effort
effort_score = 10 / estimated_hours

4. Dependencies
dependency_score = len(dependencies) * 3

Final score:
priority_score = urgency_score + importance_score + effort_score + dependency_score


Each task also returns an explanation describing why it ranks high.

🧪 Unit Tests

Located in: tasks/tests.py

Covers:

High importance

Dependencies

Low effort quick wins

Run tests:

python manage.py test

🎯 Design Decisions

Separate scoring.py for clarity

JSONField for dependencies list

Token-based authentication

Modular REST structure

Clean score explanation generator

🚀 Future Improvements

Notification system

Task categories

ML-based smart task learning

Deadline reminders

🟩 Backend README Complete