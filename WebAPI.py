# webapi.py

# Starter code for assignment 4 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Cole Thompson
# cwthomps@uci.edu
# 36762668

import json
from abc import ABC, abstractmethod
from urllib import request, error

class WebAPI(ABC):

  def _download_url(self, url: str) -> dict:
    try:
      response = request.urlopen(url)
      json_results = response.read()
      r_obj = json.loads(json_results)
      return r_obj
    
    except:
      print("You could not connect to the url.")
      quit()
	
  def set_apikey(self, apikey:str) -> None:
    '''
    Sets the apikey required to make requests to a web API.
    :param apikey: The apikey supplied by the API service
    '''
    self.apikey = apikey
	
  @abstractmethod
  def load_data(self):
    pass
	
  @abstractmethod
  def transclude(self, message:str) -> str:
    pass
