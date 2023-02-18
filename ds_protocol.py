# ds_protocol.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Cole Thompson 
# cwthomps@uci.edu 
# 36762668 

import json
from collections import namedtuple

# Namedtuple to hold the values retrieved from json messages.
DataTuple = namedtuple('DataTuple', ['type','message'])


def extract_json(json_msg:str) -> DataTuple:
  '''Call the json.loads function on a json string and convert it to a DataTuple object.'''
  try:
    json_obj = json.loads(json_msg)
    type = json_obj['response']['type']
    message = json_obj['response']['message']
  except json.JSONDecodeError:
    print("Json cannot be decoded.")

  return DataTuple(type, message)


def _response(resp):
  """This function calls the extract_json function and returns True or False."""
  response_tuple = extract_json(resp)
  res = json.loads(resp)

  if response_tuple.type == "error":
    print(response_tuple.message)
    return False
  else:
    print(response_tuple.message)
    return True
