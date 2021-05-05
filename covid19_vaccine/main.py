from flask import Flask, request,render_template, url_for ,redirect, session
from flask_session import Session
import covid_bl as businesslayer

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
# app.secret_key = "abc"

# if request.method == 'POST' :
#     singup=request.form
#     username=singup['user']
#     password=singup['pass']
#     session['username']=request.form['user']
#     if 'username' in session:
#         s=session['username']


@app.route('/')
def login():
    return render_template('loginpage.html', status = 0, val = 0)

@app.route('/home')
def clickhome():
    if not session.get("user"):
        return redirect("/")
    return render_template('test.html')

@app.route('/home',methods=['GET', 'POST'])
def home():
    uid = request.form['userid']
    pword = request.form['password']
    # print(uid, pword)
    result = businesslayer.check_user(uid, pword)
    if result == 0:
        return render_template('loginpage.html', status = 0, val = 1)
    elif result == 1:
        return render_template('loginpage.html', status = 0, val = 2)
    else:
        if request.method == "POST":
            session["user"] = request.form.get("userid")
            if not session.get("user"):
                return redirect("/loginpage")
            return render_template('test.html')
        return render_template('loginpage.html', status = 0, val = 2)


@app.route('/signup',methods=['GET', 'POST'])
def signup():
    return render_template('loginpage.html', status = 1 , val = 0)

@app.route('/signedup',methods=['GET', 'POST'])
def signedup():
    name = request.form['name']
    uid = request.form['userid']
    password = request.form['password']
    conpassword = request.form['conpassword']
    # print(name, uid, password)
    result = businesslayer.signupDetails(name, uid, password, conpassword)
    if result == 0:
        return render_template('loginpage.html', status = 1, val = 4)
    elif result == 1:
        return render_template('loginpage.html', status = 1, val = 2)
    businesslayer.insert_userDetails(name, uid, password)
    if not session.get("user"):
        return redirect("/")
    return render_template('loginpage.html', status = 0, val = 3)

@app.route('/showvac')
def show_vac():
    if not session.get("user"):
        return redirect("/")
    return render_template('getDetails.html', data=[], status=0, val = 2)

@app.route('/vaccine_details', methods = ['GET', 'POST'])
def displayDetails():
    vaccine_name = request.form['vac_name']
    checkbox = request.form.get('check_box')
    # print(vaccine_name, checkbox)
    if checkbox == None:
        data,status = businesslayer.show_details(vaccine_name)
        if not session.get("user"):
            return redirect("/")
        return render_template('getDetails.html', data=data,status=status, val=0)
    else :
        data,status = businesslayer.show_full_table_details(vaccine_name)
        if not session.get("user"):
            return redirect("/")
        return render_template('getDetails.html', data=data,status=status, val=1)

@app.route('/update_details_first_page', methods = ['GET', 'POST'])
def update_details_first_page():
    if not session.get("user"):
        return redirect("/loginpage")
    return render_template('updateDetails.html', val=1, data=[])


@app.route('/update_details', methods = ['GET', 'POST'])
def update_details():
    val = request.form.get("first-choice")
    if val == "Vaccine Names":
        data = businesslayer.only_vac_name()
        if not session.get("user"):
            return redirect("/loginpage")
        return render_template('updateDetails.html', val=2, data=data)
        if not session.get("user"):
            return redirect("/loginpage")
    return render_template('updateDetails.html', val=1, data=[])

@app.route('/update_vac_details', methods = ['GET', 'POST'])
def update_vac_details():
    val = request.form.get("second-choice")
    # vac_name = "val"
    data, val = businesslayer.show_details(val)
    if not session.get("user"):
        return redirect("/loginpage")
    return render_template('updateDetails.html', val=3, data=data)

@app.route('/updated_vaccine_details', methods = ['GET', 'POST'])
def updated_vaccine_details():
    vname = request.form['vaccine_name']
    vby = request.form['vaccine_manufactured_by']
    vplace = request.form['vaccine_manufactured_place']
    vdate = request.form['vaccine_manufactured_date']
    vexpiry = request.form['vaccine_expiry_date']
    print(vname, vby, vplace, vdate, vexpiry)
    businesslayer.update_by_vac_name(vname, vby, vplace, vdate, vexpiry)
    if not session.get("user"):
        return redirect("/loginpage")
    return render_template('updateDetails.html', val=4, data=[])
    

@app.route('/first1',methods=['GET','POST'])
def first1():
    if not session.get("user"):
        return redirect("/")
    return render_template('first1.html')

# def display_on_console(vaccine_name,city_name,ava_date,vacc_qty,expiry_date):
#     print("Vaccine Name :\t",vaccine_name)
#     print("Available In :\t",city_name)
#     print("Date :\t",ava_date)
#     print("Vaccine Qty :\t",vacc_qty)
#     print("Expiry Date :\t",expiry_date)

@app.route('/first2',methods=['GET','POST'])
def first2():
    print("Inside first2")
    _vac_name = request.form['fname']
    ava_detail = request.form['dname']
    ava_manufacture_loc = request.form['lname']
    manufacture_date = request.form['mname']
    ex_date = request.form['ename']
    print(_vac_name, ava_detail, ava_manufacture_loc, manufacture_date, ex_date)
    businesslayer.input_table1(_vac_name, ava_detail, ava_manufacture_loc, manufacture_date, ex_date)
    print("Calling HTML Page in app route first 2")
    if not session.get("user"):
        return redirect("/")
    return render_template('first1.html')

@app.route('/second2',methods=['GET', 'POST'])
def second2():
    print('inside second 2 main.py')
    if not session.get("user"):
        return redirect("/")
    return render_template('second2.html')

@app.route('/second1',methods=['GET','POST'])
def second1():
    print('inside main.py 1')
    _vac_name = request.form['vname']
    av_city = request.form['aname']
    av_date = request.form['avname']
    exp_date = request.form['nname']
    qtn_vacc = request.form['qname']
    print('inside main.py 2')
    print(_vac_name, av_city, av_date, exp_date, qtn_vacc)
    businesslayer.input_table2(_vac_name, av_city, av_date, exp_date, qtn_vacc)
    if not session.get("user"):
        return redirect("/")
    return render_template('second2.html')

@app.route('/third',methods=['GET','POST'])
def third():
    if not session.get("user"):
        return redirect("/")
    return render_template('third.html')

def third3():
    if not session.get("user"):
        return redirect("/")
    return render_template('third.html')

@app.route("/logout")
def logout():
    session.pop('user', None)
    return render_template('loginpage.html', status = 0, val = 0)
    # return render_template('loginpage.html', status = 0, val = 0)

@app.route('/contact1',methods=['GET','POST'])
def contact():
    return render_template('contact.html')

def output(c_name,c_mail,c_addres):
    print("Name:\t",c_name)
    print("E-mail :\t",c_mail)
    print("Address :\t",c_addres)


@app.route('/contact',methods=['GET','POST'])
def contact1():

    c_name = request.form['name']
    c_mail = request.form['mail']
    c_addres = request.form['addres']
    output(c_name,c_mail,c_addres)
    businesslayer.insert_contact(c_name,c_mail,c_addres)
    #print(c_name,c_mail,c_addres)
    #businesslayer.input_tabel2(c_name,c_mail,c_addres)
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(threaded=True,debug=True)

