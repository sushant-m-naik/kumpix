from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
import pickle as p
from extension import dbsq
# from firebase_functions import https_fn

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///usr.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
dbs = SQLAlchemy()
dbs.init_app(app)
from usr import usr

class dbsq(dbs.Model):
    nmd=dbs.Column(dbs.String(200),nullable=False)
    emd=dbs.Column(dbs.String(200),nullable=False, primary_key=True)
    pswd=dbs.Column(dbs.String(200),nullable=False)

    def __repr__(self) -> str:
        return f"{self.nmd} - {self.emd}"
    

@app.route("/")
def hi():
    try:
        with open("usr/usr.db","rb") as db:
               data=p.load(db)
               # print(data)
               # print("lop" in data)
               # print("Email" in data)
               # if data=={"Name":nm,"Email":em,"Password":psw}:
               if ("Email" in data) and ('Password' in data):
                   return render_template("index.html")
    except:
        return render_template("login.html")
    

# @https_fn.on_request()
# def kumpix_backend(req: https_fn.Request) -> https_fn.Response:
#     with app.request_context(req.environ):
#         return app.full_dispatch_request()



@app.route("/profile")
def hiop():
    # try:
        with open("usr/usr.db","rb") as db:
               data=p.load(db)
            #    # print(data)
            #    print("lop" in data)

            #    data= dbsq

               # print("Email" in data)
               # if data=={"Name":nm,"Email":em,"Password":psw}:
               if (("Email" in data) and ('Password' in data)) and ((data['Email'] != 'undefined') and (data['Name'] != 'undefined')):
                    # print("#")
                    dtbs= dbsq.query.all()
                    print(dtbs)
                    return render_template("profile.html", dtbs=dtbs)
               else:
                    return render_template("login.html")

    # except EOFError:
    #     return render_template("login.html")
                    # return "hi, hlo"
                    # return render_template("index.html")



@app.route("/createacc", methods=["GET","POST"])
def createacc():
    if request.method=="POST":
        nm = request.form['nm']
        em = request.form['em']
        psw = request.form['psw']
        # print("your Email is:"+em+" "+nm+" "+ psw)
        usr.user().userr(nm,em,psw)
        userd= dbsq(nmd=nm,emd=em,pswd=psw)
        dbs.session.add(userd)
        dbs.session.commit()

    
    return render_template("createacc.html")

@app.route("/db")
def ko():
    with open("usr/usr.db",'rb') as df:
         dtbs= dbsq.query.all()
    #      print(dtbs)


        #  data=p.load(df)
        #  with open("templates/db.html", "w") as dbh:
             
        #      dbh.write(str(data))

    return render_template("db.html", dtbs=dtbs)

@app.route("/login", methods=["GET","POST"])
def loginn():
    

    if request.method=="POST":
        nm = request.form['nm']
        em = request.form['em']
        psw = request.form['psw']

       
        # print("your Email is:"+em+" "+nm+" "+ psw)
        return usr.user().loginuserr(nm,em,psw)
    
    elif request.method=="GET":
        return render_template("login.html")

    # return "hi, hlo"
    return render_template("login.html")


if (__name__=="__main__"):
    app.run(debug=True)
    