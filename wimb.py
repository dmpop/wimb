#!/usr/bin/python
import sqlite3, os
from bottle import route, redirect, run, debug, template, request, static_file

@route('/wimb')
def wimb():
    if os.path.exists('wimb.sqlite'):
        conn = sqlite3.connect('wimb.sqlite')
        c = conn.cursor()
        c.execute("SELECT id,item, serial_no FROM wimb")
        result = c.fetchall()
        c.close()
        output = template('wimb.tpl', rows=result)
        return output
    else:
        conn = sqlite3.connect('wimb.sqlite')
        conn.execute("CREATE TABLE wimb (id INTEGER PRIMARY KEY, item char(254) NOT NULL, serial_no char(100))")
        conn.execute("INSERT INTO wimb (item,serial_no) VALUES ('Nippon Kogaku K. K. Nikomat FTn','FT3855032')")
        conn.commit()
        return redirect('/wimb')

@route('/add', method='GET')
def new_item():
    if request.GET.get('save','').strip():
        item = request.GET.get('item', '').strip()
        serial_no = request.GET.get('serial_no', '').strip()
        conn = sqlite3.connect('wimb.sqlite')
        c = conn.cursor()

        c.execute("INSERT INTO wimb (item,serial_no) VALUES (?,?)", (item,serial_no))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return redirect('/wimb')
    else:
        return template('add_item.tpl')

@route('/edit/:no', method='GET')
def edit_item(no):

    if request.GET.get('save','').strip():
        item = request.GET.get('item','').strip()
        serial_no = request.GET.get('serial_no','').strip()

        conn = sqlite3.connect('wimb.sqlite')
        c = conn.cursor()
        c.execute("UPDATE wimb SET item = ?, serial_no = ? WHERE id LIKE ?", (item, serial_no, no))
        conn.commit()

        return redirect('/wimb')
    else:
        conn = sqlite3.connect('wimb.sqlite')
        c = conn.cursor()
        c.execute("SELECT item,serial_no FROM wimb WHERE id LIKE ?", (str(no)))
        cur_data = c.fetchone()

        return template('edit_item', old=cur_data, no=no)

@route('/delete/:no', method='GET')
def delete_item(no):

    if request.GET.get('delete','').strip():
        conn = sqlite3.connect('wimb.sqlite')
        c = conn.cursor()
        c.execute("DELETE FROM wimb WHERE id LIKE ?", (no))
        conn.commit()

        return redirect('/wimb')
    else:
        return template('delete_item', no=no)

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

run(host="0.0.0.0",port=8080, debug=True, reloader=True)
