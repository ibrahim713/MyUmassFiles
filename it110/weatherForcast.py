################################################################
# A comprehensive python project for IT117 - showing how to use
# pyowm to generate meta data of weather forecast
# You will need to finish all the missing methods
# Ask siyao.fu@umb.edu if you have any question on this
# Deadline: 4/4/2017
################################################################

import sys
import pyowm
print "Welcome to Your Name's weather report system"

city = raw_input('Please input place information (format: city, country, such as Boston, us)\n')
myAPIKey = 'Your OWM API Key'
owm = pyowm.OWM(myAPIKey)  # You MUST provide a valid API key. See instruction for details.

# Part 1 Search for current weather in Boston (us) or any city you like
observation = owm.weather_at_place(str(city))
obs = owm.weather_at_place(str(city)) 
l = observation.get_location()
w = observation.get_weather()
print '======================================================'
print 'City information:'  # missing code
print '======================================================'
print 'City name:',   # missing code
print 'City ID:',     # missing codeALL FEATURES (1/2)
print 'City Geolocation:',  # missing code
print 'Genereal weather infor for now: ',   # missing code
# <Weather - reference time=2016-10-29 09:20, # status=Clouds>

# Part 2 Basic weather forcast information for tomorrow
forecast = owm.daily_forecast(str(city))
tomorrow = pyowm.timeutils.tomorrow()
print '======================================================'
print 'Below is the brief for tomorrow:'
print 'Sunny?',  # missing code
print 'Rainy?',  # missing code
print 'Foggy?',   # missing code
print 'Cloudy?',  # missing code
print 'Snowy?',   # missing code
print '======================================================'

# Part 3 Current weather details
print 'Current weather details'
print '======================================================'
print 'Current time:',  # missing code
print 'Wind speed and direction:',   # missing code {'speed': 4.6, 'deg': 330}
print 'Humudity level:',     # missing code        # 87
print 'Pressure:',    # missing code
print 'Weather information:',  # missing code # get detailed weather report
#print 'Detailed weather information:', w.get_detailed_status() 
print 'Temperature information:', # missing code # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# you can change fahrenheit to celsinus by changing argument 
print '======================================================'
print 'The next 7 days of weather forcast in', city, 'are as follows:'
fc = forecast.get_forecast()
# missing code
print '======================================================'

# Part 4 Search current weather observations in the surroundings of
# lat=42.32, lon=-71.04 (42.314820, -71.037695) (UMASS Boston)
print 'Weather details nearby'
print '======================================================'
observation_list = owm.weather_around_coords(42.32, -71.04)
# missing code
print '======================================================'

# Part 5 Getting weather history on a location (Boston, us) (Optional)
print 'Weather history'
print '======================================================'
# missing code
print '======================================================'


# Part 6 Dumping details to JSON or XML (Optional)
# missing code



