#!/usr/bin/python
import sqlite3
con = sqlite3.connect('wimb.db') # Warning: This file is created in the current directory
con.execute("CREATE TABLE wimb (id INTEGER PRIMARY KEY, description char(254) NOT NULL, serial_no char(100))")
con.execute("INSERT INTO wimb (description,serial_no) VALUES ('Nikon Nikomat FTn','FT3855032')")
con.commit()
