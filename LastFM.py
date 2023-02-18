# lastfm.py

# Starter code for assignment 4 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Cole Thompson
# cwthomps@uci.edu
# 36762668

import urllib, json
from urllib import request, error
from WebAPI import WebAPI
# School Project
# API key: 178dbc7f769e2e96e8d5e14a6253d7df
# Shared secret	2a8b1ae637784f4c3f746213061c986d
# Registered to	cwthomps

class LastFM(WebAPI):
    def __init__(self):
        """This initializes the LastFM class."""
        self.apikey = None
        self.artists = '\n\n'
    

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
        
        # URL for lastfm
        url = f"http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key={self.apikey}&format=json"

        try:
            # Loads in the attributes
            r_obj = self._download_url(url)
            
            for val in r_obj["artists"]["artist"]:
                self.artists += f'{val["name"]}\n'

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
            msg = message.replace("@lastfm", self.artists)
            return msg
        except:
            print('The data did not load properly.')
            quit()
