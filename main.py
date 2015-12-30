import urllib.request
import json, datetime

def getWeather(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=374e86a89388996ba4609d24c81eb7c3'
    file, header = urllib.request.urlretrieve(url)
    response = open(file)
    response = response.read()
    responseToJson = json.loads(response)
    info = responseToJson['sys']
    print(msToDate(info['sunrise']))
    
def msToDate(ms):
    return datetime.datetime.fromtimestamp(ms).strftime('%Y-%m-%d %H:%M:%S.%f')
    
getWeather('tartu')

    
    
    
