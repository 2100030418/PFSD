

from flask import Flask, render_template,request
from pymongo import MongoClient

client=MongoClient("mongodb://127.0.0.1:27017")

db=client['STUDENT']

studentdetails=db.DETAILS

app=Flask(__name__)

@app.route("/crudexample")
def sample10():
    return render_template("studentform.html")


@app.route("/success", methods=['GET', 'POST'])
def onsubmit():
    fname=request.form.get('fn')
    lname=request.form.get('ln')
    rollno=request.form.get('regno')
    mob=request.form.get('mb')
    image=request.form.get('img')

    #c={"First Name":fname,"Last Name":lname,"Regd No":rollno,"Mobile Number":mob,"Image":image}

    #studentdetails.insert_one(c)

    x={"First Name":"12345"}

    b=studentdetails.find(x)
    #a={"First Name":"chinnu"}
    #d={"$set":{"First Name": "ABD 17"}}

    #studentdetails.update_one(a,d)
    #return "Updated"

    return render_template('retrive.html', b=b)



@app.route("/retrive", methods=['GET', 'POST'])
def retrive():
    fname = request.form.get('fn')
    lname = request.form.get('ln')
    rollno = request.form.get('regno')
    mob = request.form.get('mb')

    #a={fname:"virat"}
    b=studentdetails.find(a)


    return render_template('retrive.html', b=b)

if __name__ == "__main__" :
    app.run()