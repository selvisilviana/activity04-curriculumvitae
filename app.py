'''
	AIM4 - Flask - [A] Basic - [04] Get Method
	
	Orbit Future Academy - AI Mastery - KM Batch 4
	Tim Deployment
	2023
'''

# =[Modules dan Packages]========================
from flask import Flask,render_template, redirect, url_for,request
from flask_ngrok import run_with_ngrok

# =[Variabel Global]=============================
app = Flask(_name_, static_url_path='/static')

# =[Routing]=====================================
@app.route("/")
def beranda():
	return render_template('curriculumvitae.html')	

# =[Main]========================================
if _name_ == '_main_':
    run_with_ngrok(app)
    app.run()