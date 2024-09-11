# TrackSalesBack
Task Manager's backend using Python and Django

## Prerequisites
- Python vs 3.12
- Postgresql
- Django

<br>

## Installation and execution  🛠️

1. **Fork the repository**

   Open the repository [TrackSalesBack]( ) and click the "Fork" button located in the upper right corner of the page. It creates a copy of our repository in your own Github account.
<br>

2. **Clone your forked repository**

   Open a Git Bash terminal and clone your new repository:

```bash
# Clone this repository 
git clone https://github.com/your-github-profile/your-project-name.git

```

3. **In Pycharm, open the project's directory you've just cloned**
<br> 

4. **Create the virtual environment and then activate it**

```bash
# Create the virtual environment

python -m venv venv

# Activate the virtual environment

venv\Scripts\activate

#And if you need to deactivate the virtual environment

venv\Scripts\deactivate

```
<br>

5. **Continue with the following installations**
```bash
#Install all the Python packages listed in the file requirements.txt.

pip install -r requirements.txt

#Displays information about the djangorestframework package installed in your environment

pip show djangorestframework

#Start the Django development server:

python manage.py runserver

#After installation, update the DATABASES setting in .env file

#Finally, type these commands in your terminal to manage database changes in your Django project:

python manage.py makemigrations
python manage.py migrate

```
<br>

6. **Create your branch and start working!**

```bash
#Create your branch

git checkout -b feature/yourbranchname
```
<br>
