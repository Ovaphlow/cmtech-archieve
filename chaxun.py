# -*- coding=UTF-8 -*-
from flask.views import MethodView


class ChaXun(MethodView):
    def get(self):
        from flask import render_template

        return render_template('chaxun.html')

    def post(self):
        from flask import request, render_template

        print request.form['DangAnHao']
        print request.form['ShenFenZheng']
        print request.form['XingMing']
        print request.form['XingBie']
        return render_template('chaxun.html')


class DangYueTuiXiu(MethodView):
    def get(self):
        import time
        import globalvars
        import mysql.connector
        from flask import render_template, redirect, session

        if not 'id' in session:
            return redirect('/login')

        t = time.localtime()
        time_str = time.strftime('%Y-%m', t)
        sql = 'SELECT * FROM dangan WHERE YuTuiXiuRiQi LIKE "' + time_str + '%"'
        cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
        cursor = cnx.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        return render_template('dytx.html', data=data)


class TeShuGongZhong(MethodView):
    def get(self):
        from flask import render_template, redirect, session
        import mysql.connector
        import globalvars

        if not 'id' in session:
            return redirect('/login')
        sql = 'SELECT * FROM dangan WHERE TeShuGongZhong=1'
        cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
        cursor = cnx.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        return render_template('tsgz.html', data=data)


class NvGuanLiGangWei(MethodView):
    def get(self):
        import globalvars
        import mysql.connector
        from flask import render_template, redirect, session

        if not 'id' in session:
            return redirect('/login')
        sql = 'SELECT * FROM dangan WHERE NvGuanLiGangWei=1'
        cnx = mysql.connector.Connect(**globalvars.cnx_cfg)
        cursor = cnx.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        return render_template('nglgw.html', data=data)
