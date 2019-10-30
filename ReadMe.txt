Here is the main project infrastructure

The whole machine learning part of the project was implemented in the EntertainmentPredictor.ipynb, here is where the model was trained on data from English premier leagues matches from the 2017/18 season. This was then used to predict the entertainment ratings for the English premier league 2018/19 season. All the datasets used can be found in the "data" folder.
To run this file, type the command "jupyter notebook" into your terminal which will then run Jupiter on the localhost where you can navigate to the file to open it.

The Flask backend code is mainly stored in the "main.py" file, this manages the data and distribution of the data to the correct html file. All html files are found in the "templates" folder and all the scripts, images and styles sheets can be found in the "static" folder.
To run the web application use the command "python main.py" in the terminal in the correct directory, this will then run the application on the localhost where it will act like it is running on online. This may give a warning where it recommends to use a WSGI server, I used Gunicorn for this and the command I used in my terminal to run this was: "gunicorn -w 4 -b 127.0.0.1:4000 mn:app"

Below is how I deployed this project online: (I have not stored any of the folders mentioned below in this repository)
It is best to use virtual environment so it can contain the specific needs for this project like the libraries.
You will need files like "requirements.txt", "appengine_config.py" and "app.yaml" for configuration so the site can be deployed on the google cloud platform, then you will need a "lib" folder to contain the main libraries used by the application so they can be used while running on the cloud.
To upload to cloud first activate the virtual environment then run the command "pip install -t lib -r requirements.txt" this will install the libraries needed. You can then run the command "gcloud deploy" to begin deployment to the cloud platform.
