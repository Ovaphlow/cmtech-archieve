# -*- coding=UTF-8 -*-

import gl

from flask import redirect, render_template, session, request
from sqlalchemy import text

from archman import app

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        if not 'user' in session:
            return redirect('/login')
        return render_template('home.html', User=session['user'])
    identity = request.form['identity']
    sql = '''
select
    *
from
    archive
where
    archive = :identity
    or
    identity = :identity
    '''
    param = {'identity': identity}
    res = gl.db_engine.execute(text(sql), param)
    archive = res.fetchall()
    res.close()
    if len(archive) != 1:
        return redirect('/')
    return redirect('/archive/%s' % archive[0].archive)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    sql = '''
select
    *
from
    user
where
    ZhangHao = :account
    and
    MiMa = :password'''
    param = {
        'account': request.form['account'],
        'password': request.form['password']
    }
    res = gl.db_engine.execute(text(sql), param)
    data = res.fetchall()
    res.close()
    if len(data) != 1:
        return redirect('/login')
    session['user'] = {
        'id': data[0].id,
        'account': data[0].account,
        'name': data[0].name
    }
    session['auth'] = {'amend': data[0].auth_amend}
    return redirect('/')


@app.route('/logout')
def logout():
    session.pop('user')
    session.pop('auth')
    return redirect('/login')
