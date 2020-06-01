# -*- coding: utf-8 -*-
from os import listdir, system
import re

def get_stops_times(traindata):
    tag = False
    tag_typ = ""
    index = 0
    for row in traindata:
        if row == "" or not row[0].isalpha():
            continue
        if not row.startswith((" ","Annonseras","Forts")):
            if row.startswith(("TJT ","GT ","RST ")) and "-" in row:
                tag = re.search(r'\d+', row).group()
                tag_typ = row.split(" ")[0]
            else:
                if not tag:
                    print traindata
                    exit()
                tid = re.search(r'\d+', row)
                if tid:
                    extid = row.split(tid.group())[1][2:6]
                    if not extid.isdigit():
                        extid = "0"
                    tidtext = tid.group()
                    stid = int(tidtext[:2])*60 + int(tidtext[2:])
                    if not extid == "0": 
                        etid = int(extid[:2])*60 + int(extid[2:])
                        if etid < stid:
                            extid = 24*60 - stid + etid
                        else:
                            extid = etid - stid
                    if stid < 24*60:
                        print tag_typ+","+tag + "," + str(index) + "," + row.split(" ")[0] + "," + tid.group() +","+str(extid)
                        index = index + 1

files = listdir(".")
print "tågtyp,tågnr,index,hpl,tid,stoptid"
for file in files:
    if "u.txt" in file:
        train = []
        with open(file) as f:
            content = f.read().replace("","\n").splitlines()
        tag = ""
        nytag = ""
        for row in content:
            if row.strip().startswith(("TJT ","GT ","RST ")) and "-" in row:
                nytag = re.search(r'\d+', row).group()
            if tag == nytag or tag == "":
                train.append(row)
                tag = nytag
            else:
                get_stops_times(train)
                tag = nytag
                train = [row]