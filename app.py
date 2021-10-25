
from flask import Flask, render_template, sessions, url_for, redirect, jsonify, session, request, redirect
from werkzeug.exceptions import  abort 
from werkzeug.utils import  redirect

app=Flask(__name__)

app.secret_key='secret_key_bp'

@app.route('/')
def Inicio():
    if 'username' in session:
        return f'el usuario  {session["username"] } ha hecho login'
    return 'No se ha logrado el login'

@app.route('/login', methods=['GET', 'POST'])
def Login():
    if request.method=='POST':
        usuario=request.form['username']
        session['username']=usuario
        return redirect(url_for('Inicio'))
    
    return render_template('login.html')

@app.route('/logout/')
def logout():
    session.pop('username')
    return redirect(url_for('Inicio'))