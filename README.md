# Test task to Quintagroup by Ira Shevchenko

This project will help managers monitor the activity of their colleagues.   
I tried to visually demonstrate data by task, and also added the possibility of various sorting of data by the necessary fields for easier and clearer data analysis.

---
Content
- [Installation](#Installation)
  - [Clone](#Clone)
  - [Required to install](#Required-to-install)
  - [Environment](#Environment)
  - [Setup](#Setup)
  - [How to run local](#How-to-run-local)
- [FAQ](#faq)
- [Teams](#Teams)
- [Support](#support)

----

## Installation

### Clone or Download

-  Clone this repo to your local machine using   
```
git clone https://github.com/shevchenkoira/test_task_qiuntagroup.git
```
  or download the project archive: https://github.com/shevchenkoira/test_task_qiuntagroup/archive/refs/heads/master.zip   

<a name="footnote">*</a> - to run the project you need an `.env` file with 2 fields "SECRET_KEY" and "API_KEY" in root folder 

### Required to install

- [![Python](https://docs.python.org/3.9/_static/py.svg)](https://www.python.org/downloads/release/python-3912/) 3.9.12
- Project reqirements:
```
pip install -r /requirements.txt
```

### Environment

- Add the environment variables file (.env) to the project folder.
It must contain the following settings:
```
SECRET_KEY = '😊YOUR_SECRET_KEY😊'
API_KEY='😊YOUR_CLOCKIFY_API_KEY😊'
```

----

### Setup

- Create a superuser using the terminal:    
```
python manage.py createsuperuser
```
Then enter username, email and password in terminal

----

### How to run local

- Start the terminal.
- Go to the directory "your way to the project" / test_task_quintagroup
- Run the following commands
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
- Then open http://127.0.0.1:8000/admin
- Enter your username and password created in [setup](#Setup)
- Open http://127.0.0.1:8000/admin/clockify_app/task/
- Try different sort in right side for all your analytical performance evaluation tasks
### How to run Docker

- Run our project using Docker:
```
docker-compose up
```

----

## FAQ

- The section will be filled as requests are received

----

## Team

### Development team (Ira Shevchenko)
[![@shevchenkoira](https://github.com/shevchenkoira.png?size=200)](https://github.com/shevchenkoira)

## Support

- You can contact me directly. You can go to my page in the [team section](#Team) by clicking on my avatar.
