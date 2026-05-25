import pickle as p
from flask import Flask, render_template
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy 
from extension import dbsq  # <-- Reach into the storage box safely!

usr = Blueprint('usr', __name__)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///usr.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
dbs = SQLAlchemy(app)


class user():

    def loginuserr(self,nm,em,psw):
        # name= nm
        # email=em
        # password=psw
        print("from class"+nm+em+psw)
        with open("usr/usr.db","rb") as db:
            data=p.load(db)

            gre= usr
            # print(data)
            # print("lop" in data)
            # print("Email" in data)
            # if data=={"Name":nm,"Email":em,"Password":psw}:
            if data["Email"]==em and data['Password']==psw:
                return render_template("index.html")
            else:
                return render_template("login.html")
            

    def userr(self,nm,em,psw):
        # name= nm
        # email=em
        # password=psw
        print("from class"+nm+em+psw)
        with open("usr/usr.db","wb") as db:
            p.dump({"Name":nm,"Email":em,"Password":psw},db)
            return "Successful"
        userd= dbsq(nmd=nm,emd=em,pswd=psw)
        dbs.session.add(userd)
        dbs.session.commit()

    def usrd():
         
        with open("usr/usr.db","rb") as db:
            data=p.load(db)



