
from flask import Flask, render_template, sessions, url_for, redirect, jsonify, session
from werkzeug.exceptions import  abort 
from werkzeug.utils import  redirect

app=Flask(__name__)

app.secret_key='secret_key_bp'

@app.route('/')
def Inicio():
    if 'username' in session:
        return 'el usuario ha hecho login'
    return 'No se ha logrado el login'

@app.route('/login', methods=['GET', 'POST'])
def Login():
    return render_template('login.html')
