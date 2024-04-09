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

Create a .env file and add following content
```bash
SECRET_KEY=qwertyuioplkjhgfdsazxcvbnm!@$%^&^@$!@$!@c!ss%6^&f5h!89u4w-v^64n^5^qpno7t&_7%vm9AP4Ch1BVMqrIBccv2W0loNbbyL6vxQ1w@dpgoo3va@z%us$hqu18b9!1*&8x9!5tnw78m)jkt5=j-i1f&21%c&
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
python manage.py runserver
```
