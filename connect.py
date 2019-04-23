#!/bin/python3

import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'toko_mainan'
)

if db.is_connected:
    print ("Berhasil konek ke database...!")