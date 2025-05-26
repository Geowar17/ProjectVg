
# 🛠 Vigía Project — Project and Task Management System

## 🔍 Overview

**Vigía** is a web application built with Django, designed to streamline project and task management through a clean, visual, and interactive experience. It includes a dynamic Kanban board that helps users clearly track the progress of tasks through customizable stages.

---

## ✨ Key Features

### 📁 Project Management
- Create and manage projects with key details such as contact info, address, and project owner.

### ✅ Task Management
- Associate tasks with projects and users.
- Define task priority, due dates, and detailed descriptions.

### 📌 Customizable Stages
- Organize tasks into process stages like **To Do**, **In Progress**, and **Completed**.
- Flexible stage creation and editing based on your workflow.

### 📊 Interactive Kanban View
- Visual Kanban board showing all stages—even empty ones.
- Easily drag and drop or click to move tasks between stages.

### 👥 User Management
- User registration and authentication.
- Tasks are assigned to specific users to ensure accountability.

---

## ⚙️ Technologies Used

- **Backend**: Django 4.2
- **Database**: MySQL (default)
- **Frontend**: HTML, CSS, Bootstrap 5
- **Authentication**: Built-in Django authentication system

---

## 🎯 Project Goal

The main goal of **Vigía** is to provide a visual and intuitive tool for tracking task progress within collaborative or personal projects. It is especially suited for teams that need a lightweight, effective way to organize tasks, monitor workflow, and stay productive.

---

## 📌 Status

🟢 In active development — open to improvements and new features.

---

## 📁 Folder Structure (Example)

```
vigia/
├── core/                # Main app: Projects, Tasks, Stages
├── users/               # Custom user model and authentication
├── templates/           # HTML templates
├── static/              # CSS, JS, images
├── db.sqlite3 / MySQL   # Default database
├── manage.py
└── README.md
```

---

## 🚀 Getting Started (Development)

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/vigia.git
cd vigia
```

2. **Create a virtual environment and install dependencies:**
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
```

3. **Run migrations and start the server:**
```bash
python manage.py migrate
python manage.py runserver
```

4. **Access the app:**
```
http://localhost:8000/
```

---

## 🙋‍♂️ Author

**Geovanny (Geowar17)**  
GitHub: [https://github.com/Geowar17](https://github.com/Geowar17)

---

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).
