🍽️ Multi-Restaurant Food Menu Platform

A dynamic web application built using Django and PostgreSQL that allows multiple restaurants to manage their menu items while users can browse food from different restaurants in one place.

🚀 Features
🛠 CRUD Operations – Create, view, update, and delete menu items
🔐 User Authentication – Secure login and role-based access control
🏪 Multi-Restaurant Support – Different users can manage their own menus
📄 Pagination – Efficient handling of large datasets
⚡ Caching – Improved performance and faster response times
🗂 Data Fixtures – Easy database setup and testing
🖼 Image Upload – Add images for food items
🔒 Authorization – Only owners can edit/delete their items
🛠️ Tech Stack
Backend: Python, Django
Database: PostgreSQL (can also run on SQLite for development)
Frontend: HTML, CSS (Django Templates)
Other: Django ORM, Middleware, Pagination, Caching
🧠 Concepts Implemented
Django Class-Based Views (CBVs)
Request–Response Lifecycle
ORM-based Database Interaction
Role-Based Access Control
Middleware Usage
Performance Optimization (Caching)
📂 Project Structure
food-menu-project/
│── food_menu_project/     # Main project settings
│── myapp/                 # Core app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── templates/
│── users/                 # Authentication logic
│── manage.py
│── requirements.txt
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/setushankhdhar/food-menu-project.git
cd food-menu-project
2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Apply migrations
python manage.py migrate
5️⃣ Run server
python manage.py runserver
🔑 Environment Variables

Create a .env file and add:

SECRET_KEY=your_secret_key
DEBUG=True

⚠️ Do not push .env to GitHub.

📸 Future Improvements
🔍 Search & filtering functionality
🌐 REST API using Django REST Framework
🎨 Improved UI (Bootstrap / React)
☁️ Deployment (Render / AWS)
⭐ Ratings & reviews system

Output-
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/0e3a7b90-6ccf-477b-ad76-61f8fdd88c93" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/53df3a5c-bc90-46a2-8f7c-8e3aac4d597e" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/cdd5cd0a-b815-4f91-b3c8-06bc0abb2d39" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1fcf8ead-81fc-4043-963b-e6e3d3386970" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1d017b1d-a70b-4052-b4bb-e0ca46579093" />


👨‍💻 Author
Setu Shankhdhar
