# -*- coding: utf-8 -*-
from gevent import monkey
monkey.patch_all()
from gevent.pywsgi import WSGIServer
from pymongo import MongoClient
import json

client = MongoClient()
db = client["sweden"]
kommun = db.kommun
jvg = db.jvg
distrikt = db.distrikt
ort = db.ort
platser = db.platser

def getKommun(pos):
    kommundata = kommun.find_one({
  "geometry": {
     "$geoIntersects": {
        "$geometry": {
           "type": "Point" ,
           "coordinates": pos
        }
     }
  }
    })
    return kommundata

def getDistrikt(pos):
    distriktdata = distrikt.find_one({
  "geometry": {
     "$geoIntersects": {
        "$geometry": {
           "type": "Point" ,
           "coordinates": pos
        }
     }
  }
    })
    return distriktdata

def getJvgNear(pos):
    jvgdata = jvg.find({
  "geometry": {
     "$near": {
        "$geometry": {
           "type": "Point" ,
           "coordinates": pos
        },
        "$maxDistance": 500
     }
  }
    })
    for track in jvgdata:
        yield {'properties':track['properties'],'geometry':track['geometry']}

def getJvgFobinding(namn):
    jvgdata = jvg.find({"properties.PlatsForb":namn})
    for track in jvgdata:
        yield {'properties':track['properties'],'geometry':track['geometry']}

def getPlats(pos):
    platsdata = platser.find_one({
  "geometry": {
     "$near": {
        "$geometry": {
           "type": "Point" ,
           "coordinates": pos
        },
        "$maxDistance": 10000
     }
  }
    })
    return platsdata

def application(env, start_response):
    if env['PATH_INFO'].startswith('/track/'):
        start_response('200 OK', [('Content-Type', 'application/json')])
        pos = env['PATH_INFO'].split('/')[-1].split(",")
        pos[0] = float(pos[0])
        pos[1] = float(pos[1])
        trackdata = {"tracks":[]}
        for track in getJvgNear(pos):
            trackdata["tracks"].append(track)
        return [json.dumps(trackdata)]

    elif env['PATH_INFO'].startswith('/track-connection/'):
        start_response('200 OK', [('Content-Type', 'application/json')])
        name = env['PATH_INFO'].split('/')[-1]
        trackdata = {"tracks":[]}
        for track in getJvgFobinding(name):
            trackdata["tracks"].append(track)
        return [json.dumps(trackdata)]

    start_response('404 Not Found', [('Content-Type', 'text/html')])
    return [b'<h1>Not Found</h1>']


if __name__ == '__main__':
    print('Serving on 7891...')
    WSGIServer(('', 7891), application).serve_forever()