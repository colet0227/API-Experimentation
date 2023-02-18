# openweather.py

# Starter code for assignment 4 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Cole Thompson
# cwthomps@uci.edu
# 36762668

import urllib
from urllib import error
from WebAPI import WebAPI
# Key: 5406ce4034c87029fdd6d35f8def8e13

class OpenWeather(WebAPI):
    def __init__(self, zipcode='92697', ccode='US'):
        """This initializes the OpenWeather class, setting all the required stats for this assignment."""
        self.zipcode = zipcode
        self.ccode = ccode
        self.apikey = None
        self.temperature = None
        self.high_temperature = None
        self.low_temperature = None
        self.longitude = None
        self.latitude = None
        self.description = None
        self.humidity = None
        self.city = None
        self.sunset = None
    

    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.
            
        '''
        response = None
        r_obj = None
        if self.apikey == None:
            # This error only occurs when the user decivdes to load the data before setting an api key
            print("You didn't enter a valid API key.")
            quit()
        
        # URL for openweather
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={self.zipcode},{self.ccode}&appid={self.apikey}"

        try:
            # Loads in the attributes
            r_obj = self._download_url(url)

            self.temperature = r_obj['main']['temp']
            self.high_temperature = r_obj['main']['temp_min']
            self.low_temperature = r_obj['main']['temp_max']
            self.longitude = r_obj['coord']['lon']
            self.latitude = r_obj['coord']['lat']
            self.description = r_obj['weather'][0]['description']
            self.humidity = r_obj['main']['humidity']
            self.city = r_obj['name']
            self.sunset = r_obj['sys']['sunset']

        except error.HTTPError as e:
            print('Failed to download contents of URL')
            print('Status code: {}'.format(e.code))
            quit()
        
        except urllib.error.URLError:
            print('Loss of connection')
            quit()

        finally:
            if response != None:
                response.close()
        
        return r_obj
    

    def transclude(self, message:str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
            
        :returns: The transcluded message
        '''
        try:
            msg = message.replace("@weather", self.description)
            return msg
        except:
            print('The data did not load properly.')
            quit()