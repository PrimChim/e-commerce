# e-commerce

## Setup and installation

Install my-project with npm

Clone project

```bash
git clone https://github.com/PrimChim/e-commerce.git
```

Go to project directory

```bash
cd e-commerce
```

## Make a virtual environment

```bash
python -m venv venv
```

Activate the environment

```bash
source venv/bin/activate
```

OR

```bash
venv\Scripts\activate
```

## Install requirements from requirements.txt

```bash
pip install -r requirements.txt
```

Now you are ready to use project database is set to db.sqlite3 so you can migrate and use it or you can change it

```bash
python manage.py migrate
```

Runserver

```bash
python manage.py Runserver
```
