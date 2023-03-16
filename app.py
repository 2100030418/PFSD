#import packages


from flask import Flask, render_template, redirect, url_for, request

#Creating an Instance
app=Flask(__name__)

#Route/Rendering   -Normal Route
@app.route("/")
def sample():
    return "WELCOME TO FLASK"

#Route/Rendering   -Dynamic Route
@app.route("/<name>")
def sample1(name):
    return f'HI {name}'

#Template Rendering
@app.route("/template")
def sample2():
    return render_template("ab.html")

@app.route("/card")
def card():
    return render_template("card.html")

@app.route("/template1/<name>")
def sample3(name):
    return render_template("index1.html", name=name)

#redirect
@app.route("/route/template2/<role>")
def sample4(role):
    if role=="guest":
        return redirect(url_for('sample2'))
    else:
        return redirect(url_for('sample3', name=role))


#List Rendering
@app.route("/list/rendering")
def sample5():
    lst=["ABC","DEF","GHI"]
    return render_template('index2.html', lst=lst)


#Template Inheritance
@app.route("/greetings/abc")
def sample6():
    lst=["UVW", "XYZ"]
    return render_template('index3.html', lst=lst)

#Conditional Rendering Using if cond / if tag
@app.route("/contional/def")
def sample7():
    return render_template('index4.html', value=1)

#form
@app.route("/form/studentform")
def sample8():
    return render_template('form.html')


#Form data Handling Using Flask
@app.route("/form/datahandling", methods=['GET', 'POST'])
def sample9():
    if request.method=="POST":
        name=request.form.get('stud_name')
        number=request.form.get('stud_no')  
        return name
    return render_template('studentdetails.html')


if __name__ == "__main__" :
    app.run()

