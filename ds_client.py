# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Cole Thompson 
# cwthomps@uci.edu 
# 36762668 

import socket
import ds_protocol
import json, time

def send(server:str, port:int, username:str, password:str, message:str, bio:str=None):
  '''
  The send function joins a ds server and sends a message, bio, or both

  :param server: The ip address for the ICS 32 DS server.
  :param port: The port where the ICS 32 DS server is accepting connections.
  :param username: The user name to be assigned to the message.
  :param password: The password associated with the username.
  :param message: The message to be sent to the server.
  :param bio: Optional, a bio for the user.
  '''

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    try:
      # Connect to the server
      c.settimeout(3)
      c.connect((server, port))
      print(f"client connected to {server} on {port}")
    except:
      print("Was not able to connect to server/port.")
      return False

    try:
      # Get the token and join the server
      token = join(c, username, password)
      if not token:
        return False
    except:
      print()
      return False

    # Check if the message or bio is not valid
    x = _msg_bio(message, bio)
    if x == False:
      return False

    m = message.strip(" ")
    if m == "" and bio != None:
      #bio function
      _bio(c, bio, token)
      pass
    elif bio == None:
      #post function
      post(c, message, token)
      pass
    else: 
      #bio and post function
      post(c, message, token)
      _bio(c, bio, token)
      pass
      
    return True


def _msg_bio(message, bio):
  """Check if the message or bio is not valid."""
  m = message.strip(" ")
  if (m == "" and bio == None):
    print("You didn't input a valid message.")
    return False
  
  if m == "" and bio == "":
    print("You didn't input a valid message or bio.")
    return False
  
  try:
    x = bio.strip(" ")
  except:
    x = "test"
  
  if x == "":
    print("You didn't input a valid bio.")
    return False


def join(client, username, password):
  """This is used to either join as an existing user or create a new user."""
  join_msg = {"join": {"username": username,"password": password, "token":"ok"}}
  resp = _connect(join_msg, client)
  msg = json.loads(resp)
  x = ds_protocol._response(resp)

  if not x:
    return False
  return msg["response"]["token"]


def post(client, message, token):
  """This function posts a message to the server given a token and message."""
  stamp = time.time() # Create a timestamp
  post_msg = {"token": token, "post": {"entry": message, "timestamp": stamp}}
  resp = _connect(post_msg, client)
  ds_protocol._response(resp)


def _bio(client, bio, token):
  """This function sends the bio to the server."""
  bio_msg = {"token": token, "bio": {"entry": bio, "timestamp": ""}}
  resp = _connect(bio_msg, client)
  ds_protocol._response(resp)


def _connect(msg, client):
  """This function sends a message to the server and returns the json response."""
  m = json.dumps(msg)
  send = client.makefile('w')
  recv = client.makefile('r')

  send.write(m + '\r\n')
  send.flush()

  resp = recv.readline()
  return resp
