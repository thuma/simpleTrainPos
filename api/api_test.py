# -*- coding: utf-8 -*-
import api
    
def test_jvg_find():
    for data in api.getJvgNear([16.839193333333334, 59.94326016666667]):
    	assert data['geometry']['type'] == 'LineString'

def test_jvg_forb_find():
    for data in api.getJvgFobinding('Åm'):
    	assert data['geometry']['type'] == 'LineString'

def test_kommun_find():
    assert api.getKommun([16.839193333333334, 59.94326016666667])['properties']['KOM_KOD'] == '0331'

def test_distrikt_find():
    assert api.getDistrikt([16.839193333333334, 59.94326016666667])['properties']['DISTRKOD'] == 215147

def test_plats_find():
    assert api.getPlats([12.3245781, 57.0333439])['properties']['TEXT'].encode('utf8') == 'Galtabäck'

