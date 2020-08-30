import json
import requests

def getLatLng(addr):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query='+addr
    headers = {"Authorization": "b8d8fe78bf49048b590334177f6ae431"}
    result = json.loads(str(requests.get(url,headers=headers).text))
    match_first = result['documents'][0]['address'] 
    return float(match_first['y']),float(match_first['x'])

getLatLng('경기도 의정부시 신촌로 63번길 21')