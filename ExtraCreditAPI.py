# ExtraCreditAPI.py

# Starter code for assignment 4 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Cole Thompson
# cwthomps@uci.edu
# 36762668

import urllib, json
from urllib import request, error
from WebAPI import WebAPI
# Private Key: 02bb3a5380ed7962445a142b16fcef9c0938cbe1

EXTRACREDITAPIKEY = '237'

class ExtraCreditAPI(WebAPI):
    """
    This extra credit class essentially retrieve all the players from 1979 to the present and depending on the key inputted,
    you will receive a players first name, last name, position, and weight.

    """
    def __init__(self):
        """This initializes the ExtraCreditAPI class."""
        self.first_name = None
        self.last_name = None
        self.position = None
        self.weight = None
        self.apikey = None
    

    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.
            
        '''
        response = None
        r_obj = None
        if not self.apikey.isdigit():
            # This error will occur if the user types nodigit characters in the response
            print("The API key needs to be an integer.")
            quit()
        
        if self.apikey == None or (int(self.apikey) < 1 or int(self.apikey) > 3092):
            # This error occurs when the user doesn't set an api key or it is an invalid integer not between [1, 3092]
            print("You didn't enter a valid API key.")
            quit()
        
        # URL for balldontlie extra credit
        url = f"https://www.balldontlie.io/api/v1/players/{self.apikey}"


        try:
            # Loads in the attributes
            r_obj = self._download_url(url)

            self.first_name = r_obj["first_name"]
            self.last_name = r_obj["last_name"]
            self.position = r_obj["position"]
            self.weight = r_obj["weight_pounds"]

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
            msg = message.replace("@extracredit", (self.first_name + " " + self.last_name))
            return msg
        except:
            print('The data did not load properly.')
            quit()
