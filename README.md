# Task Management Backend
This project is a **Task Management System** built with **Django** and **Django REST Framework (DRF)**. The logic for task columns (To Do / In Progress / Completed) and progress percentages follows the Figma design exactly.
## Features
- List tasks (`GET /api/list/`)
- Update tasks (`PATCH /api/update/<id>/`)
- Task fields:
  - Title (`title`)
  - Description (`description`)
  - Progress percentage (`progress`)
  - Creator (`creator`)
  - Assigned user (`assigned`)
  - Status (`status`)
- Column and progress logic:
  - **New Task** → Column `To Do` with `progress = 0`
  - **Task in `In Progress`** → Minimum `progress = 1`
  - **Task in `Completed`** → `progress = 100`
  - If progress is manually set to 100 → status automatically changes to `Completed`
## Installation & Setup
### 1. Clone the project
```bash
git clone <repo-url>
cd <project-folder>
```
### 2. Create a virtual environment
```bash
python -m venv env
source env/bin/activate  # Linux / Mac
env\Scripts\activate     # Windows
```

### 3. Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

Server will be available at: `http://127.0.0.1:8000/`

## API Endpoints
| Method | Endpoint           | Description          |
|--------|------------------|--------------------|
| GET    | /api/token/        | Get a JWT token     |
| GET    | /api/refresh/      | Refresh a JWT token |
| GET    | /api/list/         | List all tasks      |
| PATCH  | /api/update/<id>/  | Update a task       |
| POST   | /api/create/       | Create a new task   |
| DELETE | /api/delete/<id>/  | Delete a task       |

> Only the task creator can delete their tasks.
> Only the task creator or assigned user can update their tasks.

## Backend Logic
- New Task: status=`TODO`, progress=0  
- Progress 1–99: status automatically becomes `IN_PROGRESS`  
- Progress = 100 or status = COMPLETED: progress=100, status=`COMPLETED`  
- Status updated manually: progress adjusts automatically to match column logic

## Docker Setup (Optional)
### Build and run container
```bash
docker build -t task-backend .
docker run -p 8000:8000 task-backend
Development server runs at `http://localhost:8000`
```
