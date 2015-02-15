#!/usr/bin/python
import sqlite3
from bottle import route, run, debug, template, request

@route('/wimb')
def wimb_list():
    conn = sqlite3.connect('wimb.sqlite')
    c = conn.cursor()
    c.execute("SELECT id,description, serial_no FROM wimb")
    result = c.fetchall()
    c.close()
    output = template('wimb', rows=result)
    return output

@route('/add', method='GET')
def new_item():
    if request.GET.get('save','').strip():
        item = request.GET.get('item', '').strip()
        serial_no = request.GET.get('serial_no', '').strip()
        conn = sqlite3.connect('wimb.sqlite')
        c = conn.cursor()

        c.execute("INSERT INTO wimb (description,serial_no) VALUES (?,?)", (item,serial_no))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>The new item has been added, the ID is %s</p>' % new_id
    else:
        return template('add_item.tpl')

@route('/edit/:no', method='GET')
def edit_item(no):

    if request.GET.get('save','').strip():
        description = request.GET.get('description','').strip()
        serial_no = request.GET.get('serial_no','').strip()

        conn = sqlite3.connect('wimb.sqlite')
        c = conn.cursor()
        c.execute("UPDATE wimb SET description = ?, serial_no = ? WHERE id LIKE ?", (description, serial_no, no))
        conn.commit()

        return '<p>The item number %s was successfully updated</p>' % no
    else:
        conn = sqlite3.connect('wimb.sqlite')
        c = conn.cursor()
        c.execute("SELECT description,serial_no FROM wimb WHERE id LIKE ?", (str(no)))
        cur_data = c.fetchone()

        return template('edit_item', old=cur_data, no=no)

@route('/delete/:no', method='GET')
def delete_item(no):

    if request.GET.get('delete','').strip():
        conn = sqlite3.connect('wimb.sqlite')
        c = conn.cursor()
        c.execute("DELETE FROM wimb WHERE id LIKE ?", (no))
        conn.commit()

        return '<p>The item number %s has been deleted.</p>' % no
    else:
        return template('delete_item', no=no)

run(host="0.0.0.0",port=8080, debug=True, reloader=True)