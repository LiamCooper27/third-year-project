from flask import Flask, render_template, request
from flask_mail import Mail, Message
import numpy as np
import pandas as pd

#represents current file of the web app
app = Flask(__name__) #instance of flask

app.config.update(dict(
    MAIL_SERVER = 'smtp.googlemail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    #MAIL_USERNAME = this is where the email you would like to send from will go
    #MAIL_PASSWORD = this is where the corresponding password to that email will go
))

mail = Mail(app)

epl_previous = pd.read_csv("data/E0.csv") #2017/18 games (last season)
epl_current = pd.read_csv("data/E1.csv") #2018/19 games (current season)
gathered_ratings = pd.read_csv("data/E0matchratings.csv") #2018/19 games (current season)

#called when user navigates to default page
@app.route("/", methods=("POST","GET")) #default page of the app
def home():
    upcoming = epl_current[epl_current.values == "12/05/2019"]
    recent = epl_current.loc[epl_current['Date'].isin(['03/05/2019','04/05/2019','05/05/2019','06/05/2019'])]
    return render_template('index.html', upcoming=upcoming, recent=recent)

@app.route("/ratings", methods=("POST","GET"))
def ratings():
    week = 1
    data = epl_current[epl_current.values == "M"+str(week)]

    if request.method=='POST':
        week = request.form["matchweek"]
        data = epl_current[epl_current.values == "M"+str(week)]

    return render_template("ratings.html", tables=data, week=week)

@app.route("/teams", methods=("POST","GET"))
def teams():

    team = "Arsenal"
    data = epl_current[epl_current.values == team]
    rating = round(data["MPER"].mean())

    if request.method=='POST':
        team = request.form["team"]
        data = epl_current[epl_current.values == team]
        rating = round(data["MPER"].mean())

    return render_template("teams.html", name=team, tables=data, rating=rating)

@app.route("/opinions", methods=("POST","GET"))
def opinions():

    cols = len(gathered_ratings.columns) + 1

    list = []
    if request.method=='POST':

        for i in range (0,380):
            test1 = request.form["tb"+str(i)]
            list.append(test1)

        new_col = len(gathered_ratings.columns) + 1
        gathered_ratings["P"+str(new_col)] = list
        gathered_ratings.to_csv("data/E0matchratings.csv", index=None)

        msg = Message('MatchRatings P'+str(cols), sender='goodgamecontact27@gmail.com', recipients=['liamcooper1227@gmail.com'])
        msg.body = str(list)
        mail.send(msg)

    return render_template("opinions.html", tables=epl_previous, cols= cols)

@app.route("/contact", methods=("POST","GET"))
def contact():

    if request.method=='POST':

        sname = request.form["sendername"]
        semail = request.form["email"]
        sage = request.form["age"]
        sviewing = request.form["viewinghabbit"]
        srating = request.form["designrating"]
        smessage = request.form["message"]

        msg = Message('Feedback', sender='goodgamecontact27@gmail.com', recipients=['liamcooper1227@gmail.com'])
        msg.body = "Feedback from good game: \nName = " + str(sname) + "\nEmail = " + str(semail) + "\nAge = " + str(sage) + "\nViewing Habbits = " + str(sviewing) + "\nDesign Rating = " + str(srating) + "\nFeedback = " + str(smessage)

        mail.send(msg)

    return render_template("contact.html")

# this will run when the script is run
if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="127.0.0.1",port=8080,debug=True)
