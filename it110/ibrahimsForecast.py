
import sys
import pyowm
from pyowm import timeutils

print "Welcome to Ibrahim's weather report system"

city = raw_input(
    'Please input place information (format: city, country, such as Boston, us)\n')
myAPIKey = '3841666e406d027a802239567899e71d'
owm = pyowm.OWM(myAPIKey)  # You MUST provide a valid API key

# Search for current weather in Boston (us) or any city you like
observation = owm.weather_at_place(str(city))
obs = owm.weather_at_place(str(city))
l = observation.get_location()
w = observation.get_weather()

print '======================================================'
print 'City information:'
print '======================================================'
print 'City name:', l.get_name()
print 'City ID:', l.get_ID()
print 'City Geolocation:', l.get_lat(), l.get_lon()
print 'Genereal weather info for now: ',  w

# The following method can be found in pyOWM wiki webpage.
z = owm.daily_forecast(str(city))
tomorrow = pyowm.timeutils.tomorrow()
print '======================================================'
print 'Below is the brief for tomorrow:'
print 'Sunny?', z.will_be_sunny_at(timeutils.tomorrow())
print 'Rainy?',  z.will_be_rainy_at(timeutils.tomorrow())
print 'Foggy?',   z.will_be_foggy_at(timeutils.tomorrow())
print 'Cloudy?',  z.will_be_cloudy_at(timeutils.tomorrow())
print 'Snowy?',  z.will_be_snowy_at(timeutils.tomorrow())
print '======================================================'

# Weather details
print 'Weather details'
print '======================================================'
time1 = w.get_reference_time(timeformat='iso')
print 'Current time:', (time1)

print 'Wind speed and direction:',
wind1 = w.get_wind()
print (wind1)
print 'Humudity level:',
humid1 = w.get_humidity()
print (humid1)
print 'Pressure:',
pressure1 = w.get_pressure()
print (pressure1)
print 'Weather information:',
info1 = w.get_detailed_status()
print (info1)

print 'Temperature information:'
temperature1 = w.get_temperature('celsius')
print (temperature1)

print '======================================================'
print 'The next 7 days of weather forcast in', city, 'are as follows:'
sevendays1 = owm.daily_forecast(str(city))
f1 = sevendays1.get_forecast()
for weather in f1:
    print (weather.get_reference_time('iso'), weather.get_status())

# Search current weather observations in the surroundings of
# lat=42.32, lon=-71.04 (42.314820, -71.037695) (UMASS Boston)
observation_list = owm.weather_around_coords(
    42.314820, -71.037695, limit=2)
###owm.weather_history_at_place(str(city)) # I think the weather History feature costs money
obs.to_JSON()
w.to_XML()
