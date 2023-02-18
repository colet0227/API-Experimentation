# a4.py

# Starter code for assignment 4 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Cole Thompson
# cwthomps@uci.edu
# 36762668

from ExtraCreditAPI import ExtraCreditAPI
from OpenWeather import OpenWeather
from LastFM import LastFM
from pathlib import Path
from Profile import Profile, Post
import commands
import ds_client
# [1, 3092]
# 168.235.86.101

EXTRACREDITAPIKEY = "237"
PORT = 3021

def opening():
  """This is the User Interface for posting to the server."""
  print("Welcome to DSU Server, press Q to quit at any time.")
  open = f'What server would you like to connect to?\n'
  profile_menu = f'What would you like to do next?\n\n\t1. Create a profile\n\t2. Open a profile\n'
  menu = f'What would you like to do next?\n\n\t1. Post to the server\n\t2. Go back to profile menu\n'
  post_menu = f'What would you like to do next?\nPlease note you can use @weather, @lastfm, and @extracredit\n\n\t1. Post a bio only\n\t2. Post a message only\n\t3. Post a bio and message\n'

  server = input(open)

  # Loops while the input is not Q
  while server != 'Q':
    text = input(profile_menu)

    # Verifies inout
    while text not in ('1', '2', 'Q'):
        text = input('Please provide a valid option: ')

      # Create a profile
    if text == '1':
      obj = _create(server)
      if not obj:
        print("Could not open the requested file. Terminating program.")
        quit()
      # Open a profile
    elif text == '2':
      obj = _open(server)
      if not obj:
        print('Could not open the requested file. Terminating program.')
        quit()

      # Quit
    elif text == "Q":
      break

    resp = input(menu)

    # Verifies input
    while resp not in ('1', '2', 'Q'):
      resp = input('Please provide a valid option: ')

      # Post to the server
    if resp == "1":
      posting = input(post_menu)

      #Verifies input
      while posting not in ('1', '2', '3', 'Q'):
        posting = input('Please provide a valid option: ')

      # Instantiates Profile class
      profile = Profile(server)

      # Loads the profile from the given path
      profile.load_profile(file)

      # Posts bio only
      if posting == "1":
        new_bio = bio_change()
        if new_bio == None:
          quit()
        elif new_bio == "Same":
          pass
        else:
          profile.bio = new_bio
          profile.save_profile(file)

        ds_client.send(profile.dsuserver, PORT, profile.username, profile.password, "", profile.bio)

      # Posts message only
      elif posting == "2":
        post_message = input("Enter a post message: ")

        if '@weather' in post_message:
            weather = OpenWeather()
            api_key = input('Please set an OpenWeather API key: ')
            weather.set_apikey(api_key)
            weather.load_data()
            post_message = weather.transclude(post_message)

        if '@lastfm' in post_message:
            lastfm = LastFM()
            api_key = input('Please set a LastFM API key: ')
            lastfm.set_apikey(api_key)
            lastfm.load_data()
            post_message = lastfm.transclude(post_message)

        if '@extracredit' in post_message:
            extra = ExtraCreditAPI()
            api_key = input('Please set an ExtraCreditAPI key: ')
            extra.set_apikey(api_key)
            extra.load_data()
            post_message = extra.transclude(post_message)

        profile.posts = profile.add_post(Post(post_message))
        profile.save_profile(file)
        ds_client.send(profile.dsuserver, PORT, profile.username, profile.password, post_message)

      # Posts bio and message
      elif posting == "3":
        new_bio = bio_change()
        if new_bio == None:
          quit()
        elif new_bio == "Same":
          pass
        else:
          profile.bio = new_bio
        
        post_message = input("Enter a post message: ")
        if '@weather' in post_message:
            weather = OpenWeather()
            api_key = input('Please set an OpenWeather API key: ')
            weather.set_apikey(api_key)
            weather.load_data()
            post_message = weather.transclude(post_message)

        if '@lastfm' in post_message:
            lastfm = LastFM()
            api_key = input('Please set a LastFM API key: ')
            lastfm.set_apikey(api_key)
            lastfm.load_data()
            post_message = lastfm.transclude(post_message)

        if '@extracredit' in post_message:
            extra = ExtraCreditAPI()
            api_key = input('Please set an ExtraCreditAPI key: ')
            extra.set_apikey(api_key)
            extra.load_data()
            post_message = extra.transclude(post_message)
        
        profile.posts = profile.add_post(Post(post_message))
        profile.save_profile(file)
        ds_client.send(profile.dsuserver, PORT, profile.username, profile.password, post_message, profile.bio)

    # Quit
    elif resp == "Q":
      break
  quit()


def _create(server):
  """Creates a file with a path and instantiates the Profile class with the server parameter as the dsuserver."""
  name = input('Wonderful! What name would you like to use for your file?\n') + '.dsu'
  location = input('Where would you like to store the file?\n')
  try:
      p = Path(location)
      p = p / name
      global file
      file = p

      # Open file if it already exists
      try:
          profile = Profile(server)
          profile.load_profile(p)
          print(f'File already exists!\nProfile username: {profile.username}\nProfile password: {profile.password}\nProfile bio: {profile.bio}')
          return

      # Otherwise, create the file normally
      except:
          file = commands.create_file(location, name)
          profile = Profile(server)
          profile.save_profile(file)
          profile.load_profile(file)
  except:
        print('There was an error creating your file.')
        return False
  username = input('Please enter a username (press enter to leave blank): ')
  password = input('Please enter a new password (press enter to leave blank): ')
  bio = input('Please enter a brief bio (press enter to leave blank): ')
  
  text = f" -usr '{username}' -pwd '{password}' -bio '{bio}'"
  commands.e_command(text, file)
  return True


def _open(server):
  """Opens a file and instantiates the Profile class and updates the dsuserver with the server parameter."""
  global file
  file = input('Wonderful! What is the name of the file you would like to open?\n')
  try:
      profile = Profile()
      profile.load_profile(file)
      profile.dsuserver = server
      profile.save_profile(file)
      print(f'Profile username: {profile.username}\nProfile password: {profile.password}\nProfile bio: {profile.bio}')
      return True
  except:
      print('There was an error retrieving your file.')
      return False


def bio_change():
  """Asks the user if they would like to change their bio or keep it the same and returns a value based on the input."""
  bio_menu = f'What would you like to do next?\n\n\t1. Change your bio\n\t2. Keep it the same\n'
  ans = input(bio_menu)
  while ans not in ('1', '2', 'Q'):
    ans = input('Please provide a valid option: ')
  
  # Return to quit
  if ans == "Q":
    return None
  
  # Asks for a new bio
  elif ans == "1":
    change = input("Input a new bio: ")
    return change
  
  # Does nothing
  else:
    return "Same"


if __name__ == "__main__":
    opening()
