from flask import Flask, render_template, request, redirect,url_for

def insert_into_tabel(venit, tinta):
    pass
    #conectare la db
    #executie query insert into nu stiu ce
    #commit

def login(email,password):
    
    #verifici in baza de date daca exista un record cu emailul ala si parola aia
    #returnezi true sau false in functie de rezultatul obtinut (ai date e true, nu ai date e false)
    return True


app = Flask(__name__)

@app.route("/home", methods = ['POST','GET'])
def DisplayHomePage():
    if request.method == 'POST':
        print("DisplayHomePage")
        print(request.form)
        email = request.form['email']
        password = request.form['password']
        if login(email, password) == True:
            return redirect("meniu")
        else:
            print("Login failed")
        
        
    return render_template("Autentificare.html")

@app.route("/meniu", methods = ['POST','GET'])
def meniu():
    print("DisplayMeniuPage")
    return render_template("Meniu.html")

@app.route('/info',methods = ['POST','GET'])
def DisplayInfo():
    print("DisplayInfo")
    return render_template("Info.html")

@app.route('/intro',methods = ['POST','GET'])
def DisplayIntroducereDate():
    print("DisplayIntroducereDate")
    if request.method == 'POST':
        #print(request.form)
        venit_din_html = request.form['venit']
        tinta_din_html = request.form['tinta']
        
        insert_into_tabel(venit_din_html,tinta_din_html)
        #insert data into database somewhere
        #print(venit_din_html)
        
    return render_template("IntroducereDate.html")
    

@app.route('/rezultate',methods = ['POST','GET'])
def DisplayRezultate():
    print("DisplayRezultate")
    return render_template("Rezultate.html")

@app.route('/concluzii',methods = ['POST','GET'])
def DisplayConcluzii():
    print("DisplayConcluzii")
    return render_template("Concluzii.html")

app.run(port=5000)

