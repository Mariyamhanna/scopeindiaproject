
# Scope India Website (Python Django Full Stack Project)

A full-stack educational website inspired by Scope India, featuring Home, About, Contact, FAQ, Registration, Login, and Student Dashboard pages with authentication and email support.




## Features
🏠 Home Page: Overview of the institute and offered services

ℹ️ About Us Page: Details about the institute and its mission

❓ FAQ Page: List of frequently asked questions for users’ quick help

📞 Contact Page: Contact form with SMTP email sending support

🧾 Registration Page: Secure user registration with validation

🔐 Login Page: User authentication using Django’s built-in auth

🎓 Student Dashboard: Personalized dashboard after login

✉️ Email Integration: Sends confirmation and notification emails

🍪 Cookie-Based Session: Keeps users logged in for a set duration

🧮 Admin Panel: Manage students, users, and site content easily

📱 Responsive Design: Works smoothly on desktop, tablet, and mobile

🗄️ Database Integration: Stores and manages user and contact data with SQLite

🧰 Clean UI with Bootstrap: Simple, modern, and user-friendly design

🔧 Modular Code Structure: Organized files for easy maintenance and scalability


## Tech Stack
Backend: Python 3, Django Framework

Frontend: HTML, CSS, Bootstrap

Database: SQLite3 (default Django DB)

Tools: Visual Studio Code, Git, GitHub
## Installation & Setup Instructions
1️⃣ Clone the Repository:

git clone https://github.com/Mariyamhanna/scopeindiaproject.git

cd scopeindiaproject

2️⃣ Create a Virtual Environment:

pip install virtualenv

virtualenv myenv

3️⃣ Activate the Virtual Environment:

myenv\Scripts\activate #For Windows

source myenv/bin/activate #For Mac/Linux 

4️⃣ Install Django:

pip install django

5️⃣ Apply Database Migrations:

python manage.py migrate

6️⃣ Run the Development Server:

python manage.py runserver

Open Your Browser and Go To:

http://127.0.0.1:8000/Scope/home



## Folder Structure
Django_proj/                     # Root project folder
│
├── myproject/                   # Django project folder (settings, URLs, wsgi, etc.)
│   ├── myenv/                   # Virtual environment (Python packages)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── Scope/                       # Django app
│   ├── migrations/              # Database migrations
│   ├── static/                  # CSS, JS, images
│   ├── templates/               # HTML templates
│   ├── __init__.py
│   ├── admin.py                 # Admin panel configuration
│   ├── apps.py                  # App configuration
│   ├── forms.py                 # Django forms
│   ├── models.py                # Database models
│   ├── tests.py                 # Unit tests
│   ├── urls.py                  # App URLs
│   └── views.py                 # App views
│
└── manage.py                     # Django management script (root of project)
## Version Control
This project uses Git for version control and GitHub for hosting and collaboration.

## Future Enhancements
- Add a course listing and enrollment system  
- Improve mobile responsiveness and UI design  
- Add search and filter functionality for FAQs and courses  
- Enhance admin dashboard for easier content management

## Screenshots

![1](https://github.com/user-attachments/assets/58beae6c-dfd7-441f-a8e0-816499a7d1cf)

![2](https://github.com/user-attachments/assets/2c067991-2b14-4dbf-a894-62a993a38d7b)

![3](https://github.com/user-attachments/assets/64a803d9-e631-4c9c-8ded-19b74dc201ea)

![4](https://github.com/user-attachments/assets/737c6955-ebc6-44d6-81e3-8dc879ce5060)

![5](https://github.com/user-attachments/assets/2c488216-eb89-4199-868d-abf7490feab2)

![6](https://github.com/user-attachments/assets/7ab1a40a-e8e8-42f7-948b-666e58ab62cb)

![7](https://github.com/user-attachments/assets/02780fb8-566f-4d40-841e-48d2fa3c20f0)

![8](https://github.com/user-attachments/assets/d3f9faba-91f1-4835-9b4b-c24ac088c01f)

![9](https://github.com/user-attachments/assets/18778b46-a93d-4e9b-b3e0-dac943aba6c6)

![10](https://github.com/user-attachments/assets/513022d8-472f-42b4-acec-206e808ddad0)

![11](https://github.com/user-attachments/assets/a3d2528b-8e36-4ded-9f52-af5d783cfef4)

![12](https://github.com/user-attachments/assets/9c5b0f86-cd73-4586-b573-a35ae28e6c9e)

![13](https://github.com/user-attachments/assets/a44f7021-084c-49b6-853f-2a9f54f88c55)

![14](https://github.com/user-attachments/assets/e72c14ef-1bb5-4047-b868-4068d3703470)

![15](https://github.com/user-attachments/assets/1c170b79-d667-4139-8b2d-83f5e0d8e072)

![16](https://github.com/user-attachments/assets/5b077b6b-c769-4eb5-8638-59a4ce360cf6)

![17](https://github.com/user-attachments/assets/09cbbed5-0a8e-414d-8bf6-e39574d6deb5)

![18](https://github.com/user-attachments/assets/d6031a87-cd07-4f84-b2b5-0b59aa81b166)

![19](https://github.com/user-attachments/assets/7fd74be5-766e-4551-b7c2-d5b82f7ab099)

![20](https://github.com/user-attachments/assets/18e98894-54f9-4e8c-92df-aa7d47f78c17)

![21](https://github.com/user-attachments/assets/ccfd6a7e-34b7-4164-97dc-2066412e10d1)

![22](https://github.com/user-attachments/assets/f60b6cbb-43bf-436f-b215-ada4e2e47616)

![23](https://github.com/user-attachments/assets/9cd76596-e5b5-4288-b7d5-c5780db2ea4d)



## Demo

Check out my video: [Watch Demo of My Project🔥](https://youtu.be/cgFwYrm57g4)

[![Watch Demo of My Project🔥](https://img.youtube.com/vi/cgFwYrm57g4/0.jpg)](https://youtu.be/cgFwYrm57g4)

## Contact
**Developer:** Mariyam Hanna  
**Email:** mariyamhanna2003@gmail.com  
**GitHub:** https://github.com/Mariyamhanna/scopeindiaproject.git

## License
This project was developed for learning and portfolio purposes.
You are free to explore and use it for educational or professional reference.

⭐ If you like this project, please give it a star on GitHub!

