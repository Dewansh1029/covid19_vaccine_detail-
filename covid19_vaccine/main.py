from flask import Flask, request,render_template, url_for ,redirect

#UPLAD_FLODER ='static/uploads'

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('test.html')

@app.route('/test',methods=['GET', 'POST'])
def test():
    return render_template('test.html')

@app.route('/first1',methods=['GET','POST'])
def first1():
    return render_template('first1.html')

def display_on_console(vaccine_name,city_name,ava_date,vacc_qty,expiry_date):
    print("Vaccine Name :\t",vaccine_name)
    print("Available In :\t",city_name)
    print("Date :\t",ava_date)
    print("Vaccine Qty :\t",vacc_qty)
    print("Expiry Date :\t",expiry_date)

def display_all():
    data1=[]
    """data2=[]
    data3=[]
    data4=[]
    data5=[]"""
    for i in range(len(data1)):
        _vac_name=input()
        data1.append(_vac_name)


@app.route('/first2',methods=['GET','POST'])
def first2():
    print("Inside first2")
    _vac_name = request.form['fname']
    ava_city = request.form['dname']
    ava_date = request.form['lname']
    qt_vacc = request.form['mname']
    ex_date = request.form['ename']
    display_on_console(_vac_name,ava_city,ava_date,qt_vacc,ex_date)
    print("Calling HTML Page in app route first 2")
    return render_template('first1.html')    

"""def display_all():
    data1=[]
    data2=[]
    data3=[]
    data4=[]
    data5=[]
    for i in range(len(data1)):
        _vac_name=input()
        data1.append(_vac_name)"""


@app.route('/second1',methods=['GET', 'POST'])
def second2():
    return render_template('second2.html')

def outputdisplay(vaccine_namee,available_city,available_date,quantity_vaccine,expi_date,):
    print("Vaccine Name :\t",vaccine_namee)
    print("Avaliable City :\t",available_city)
    print("Date :\t",available_date)
    print("Vaccine Qty :\t",quantity_vaccine)
    print("Expiry Date :\t",expi_date)



@app.route('/second2',methods=['GET','POST'])
def second1():
    _vac_name = request.form['vname']
    av_city = request.form['aname']
    av_date = request.form['avname']
    qtn_vacc = request.form['nname']
    exp_date = request.form['qname']

    outputdisplay(_vac_name,av_city,av_date,qtn_vacc,exp_date)
    
    return render_template('second2.html')
def dispaly_all(_vac_name,av_city,av_date,qtn_vacc,exp_date):
    print("_vac_name")
    print("av_city")
    print("av_date")
    print("qtn_vacc")

@app.route('/third1',methods=['GET','POST'])
def third():
    return render_template('third.html')
"""def display_all(_vac_name,av_city,av_date,qtn_vacc,exp_date):

    vaccine=data['_vac_name']
    city=data['av_city']
    date=data['av_data']
    quantity=data['qtn_vacc']
    expire=data['exp_date']"""
    #data=[_vac_name,av_city,av_date
"""_vac_name = request.form['vname']
    av_city = request.form['aname']
    av_date = request.form['avname']
    qtn_vacc = request.form['nname']
    exp_date = request.form['qname']
    
    data=
    vaccine=data['vname']
    city=data['aname']
    date=data['avname']
    quantity=data['nname']
    expire=data['qname']

    av_city=[]
    data.append(_vac_name)
    print("k")
    print(data)"""

@app.route('/third',methods=['GET','POST'])
def third1():
    print("a")
    """_vac_name = request.form['vname']
    av_city = request.form['aname']
    av_date = request.form['avname']
    qtn_vacc = request.form['nname']
    exp_date = request.form['qname']"""
    display_all(_vac_name,av_city,av_date,qtn_vacc,exp_date)

    vaccine=data['vname']
    city=data['aname']
    date=data['avname']
    quantity=data['nname']
    expire=data['qname']
    print(vaccine, city, date)

    return render_template('third.html',vaccine=vaccine,city=city,date=date,quantity=quantity,expire=expire)

if __name__ == '__main__':    
    # This is used when running locally. Gunicorn is used to run the
    #app.run(host='0.0.0.0', port=8080, debug=True, processes=4, threaded=True)
    app.run(threaded=True,debug=True)
    #app.run(host='127.0.0.1', port=8080, debug=True)
## [END app]

