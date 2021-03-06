#!/usr/bin/python

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sqlite3, os
from bottle import route, redirect, run, debug, template, request, static_file

@route('/')
def wimb():
    if os.path.exists('wimb.sqlite'):
        conn = sqlite3.connect('wimb.sqlite')
        conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')
        c = conn.cursor()
        c.execute("SELECT id,item, serial_no, note FROM wimb")
        result = c.fetchall()
        c.close()
        output = template('wimb.tpl', rows=result)
        return output
    else:
        conn = sqlite3.connect('wimb.sqlite')
        conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')
        conn.execute("CREATE TABLE wimb (id INTEGER PRIMARY KEY, item char(254) NOT NULL, serial_no char(100), note char(254))")
        conn.execute("INSERT INTO wimb (item,serial_no, note) VALUES ('Nippon Kogaku K. K. Nikomat FTn','FT3855032', 'ILFORD XP2 Super 400')")
        conn.commit()
        return redirect('/')

@route('/add', method='GET')
def new_item():
    if request.GET.get('add','').strip():
        item = request.GET.get('item', '').strip()
        serial_no = request.GET.get('serial_no', '').strip()
        note = request.GET.get('note', '').strip()
        conn = sqlite3.connect('wimb.sqlite')
        conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')
        c = conn.cursor()

        c.execute("INSERT INTO wimb (item,serial_no, note) VALUES (?,?,?)", (item,serial_no,note))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return redirect('/')
    else:
        return template('add_item.tpl')

@route('/edit/:no', method='GET')
def edit_item(no):

    if request.GET.get('save','').strip():
        item = request.GET.get('item','').strip()
        serial_no = request.GET.get('serial_no','').strip()
        note = request.GET.get('note','').strip()

        conn = sqlite3.connect('wimb.sqlite')
        conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')
        c = conn.cursor()
        c.execute("UPDATE wimb SET item = ?, serial_no = ?, note = ? WHERE id LIKE ?", (item, serial_no, note, no))
        conn.commit()

        return redirect('/')
    else:
        conn = sqlite3.connect('wimb.sqlite')
        conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')
        c = conn.cursor()
        c.execute("SELECT item,serial_no,note FROM wimb WHERE id LIKE ?", (no))
        cur_data = c.fetchone()

        return template('edit_item.tpl', old=cur_data, no=no)

@route('/delete/:no', method='GET')
def delete_item(no):

    if request.GET.get('delete','').strip():
        conn = sqlite3.connect('wimb.sqlite')
        conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')
        c = conn.cursor()
        c.execute("DELETE FROM wimb WHERE id LIKE ?", (no))
        conn.commit()

        return redirect('/')
    else:
        return template('delete_item.tpl', no=no)

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

run(host="0.0.0.0", port=8888, debug=True, reloader=True)
