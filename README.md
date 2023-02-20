# Capstone-Project
(( Add the project synopsis here ))

## Instructions to run local server:

Install required python packages:

```
cd API
pip install -r requirements.txt
```

To run the server:
```
cd config
python manage.py runserver
```

Once you compile and run the server, open http://127.0.0.1:8000/.
You can navigate to the main page at: http://127.0.0.1:8000/main-page/

Every time you make changes to models (database tables) you need to make migrations to the database
```
python manage.py makemigrations
python manage.py migrate
```


If you have issues installing tensorflow on windows, you may need to enable long path: https://www.howtogeek.com/266621/how-to-make-windows-10-accept-file-paths-over-260-characters/ 
