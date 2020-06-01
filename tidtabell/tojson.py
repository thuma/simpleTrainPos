# -*- coding: utf-8 -*-
import sqlite3
import json
conn = sqlite3.connect('tidtabell.db')
lista = conn.execute("""
    SELECT
        tågnr,
        hpl
    FROM
        tidtabell
    ORDER BY
        tågnr,
        i
    """)
tag = {}
for stop in lista:
    if str(stop[0]) in tag:
        tag[str(stop[0])].append(stop[1])
    else:
        tag[str(stop[0])] = [stop[1]]

print json.dumps(tag)
