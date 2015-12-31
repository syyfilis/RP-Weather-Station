import urllib.request
import json, datetime

def getWeather(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=374e86a89388996ba4609d24c81eb7c3'
    file, header = urllib.request.urlretrieve(url)
    response = open(file).read()
    responseAsJson = json.loads(response)
    return sortWeatherInfo(responseAsJson)

def msToDate(ms):
    return datetime.datetime.fromtimestamp(ms).strftime('%Y-%m-%d %H:%M:%S.%f')

def tempToCelsius(kelvin):
    return kelvin - 273.15

def sortWeatherInfo(json):#must test cloudiness, snow, rain etc. before implementing
    weather = {}
    weather['sunset'] = msToDate(getValueFromJson(json['sys'], 'sunset'))
    weather['sunrise'] = msToDate(getValueFromJson(json['sys'], 'sunrise'))
    weather['country'] = getValueFromJson(json['sys'], 'country')
    weather['windDeg'] = getValueFromJson(json['wind'], 'deg')
    weather['windSpeed'] = getValueFromJson(json['wind'], 'speed')
    weather['weatherDesc'] = getValueFromJson(json['weather'][0], 'description')
    weather['weatherMain'] = getValueFromJson(json['weather'][0], 'main')
    weather['humidity'] = getValueFromJson(json['main'], 'humidity')
    weather['temp'] = tempToCelsius(getValueFromJson(json['main'], 'temp'))
    weather['cityName'] = getValueFromJson(json, 'name')
    weather['time'] = msToDate(getValueFromJson(json, 'dt'))
    return weather

def getValueFromJson(json, key):
    return json[key]



print(getWeather('edinburg'))

    
    
    
