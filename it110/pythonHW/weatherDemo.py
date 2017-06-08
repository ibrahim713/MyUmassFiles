# simple demo showing how to use pyowm
############
# This is the part one of your Python weather report project
############

import pyowm
# You have to register on the OWM website to get an API key

myAPIKey = '3841666e406d027a802239567899e71d'

owm = pyowm.OWM(myAPIKey)  # You MUST provide a valid API key

# You have a pro subscription? Use:
# owm = pyowm.OWM(API_key='myAPIKey', subscription_type='pro')

# step 1 test your program works or not
print 'Will it be sunny tomorrow at this time in Boston (U.S.) ?'
forecast = owm.daily_forecast("Boston,us")
tomorrow = pyowm.timeutils.tomorrow()
print forecast.will_be_sunny_at(tomorrow)  # Always false in Boston right now, right? ;-)

# step 2 search for current weather in Boston (us)
observation = owm.weather_at_place('Boston,us')
w = observation.get_weather()
print 'weather in Boston'
print(w)




#Toronto weather Example
obs = owm.weather_at_place('Toronto,ca')
obs = owm.weather_at_id(5174095) # City ID for Toronto
obs = owm.weather_at_coords(43.7183937,-79.6589302)
x = obs.get_weather()
print 'weather in Toronto'
print x



         # <Weather - reference time=2016-10-29 09:20,
                              # status=Clear>

# Weather details
w.get_wind()                  # {'speed': 4.6, 'deg': 330}
w.get_humidity()              # 87
w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}


# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation_list = owm.weather_around_coords(-22.57, -43.12)
print observation_list
