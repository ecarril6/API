# Capstone Project- Kataba
(( Handwriting Recognition and Handwriting Sample Comparison ))

Google Colab Notebook Links: 

Jada Sachetti- 

Image Cropping https://colab.research.google.com/drive/19pK4YeHhuI_DLjxxy74lYXk4KzhUBr9X?usp=sharing

Feature Extraction and Model implementation https://colab.research.google.com/drive/1FYU0FcZU6zAjOhbmENlXJb4Oyi0Mp3J6#scrollTo=f5PhhAtigNbU

Image Comparison (post Siamese model training) https://colab.research.google.com/drive/1trMhaqYBv0JYmTX6iFH-xqS3goO4MYb0?usp=sharing

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


