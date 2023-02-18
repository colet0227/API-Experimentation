# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Cole Thompson 
# cwthomps@uci.edu 
# 36762668

from pathlib import Path
from Profile import Profile, Post


def e_command(text, file):
    """This will edit the profile."""
    count = 0
    profile = Profile()
    profile.load_profile(file)
    change = False

    quotes = '"'
    if "'" in text:
        quotes = "'"

    # -usr [USERNAME]
    if ' -usr ' in text:
        change = True
        count += 2
        contents = text.split(quotes)
        if " " in contents[count - 1]:
            print('Username should not have whitespace!')
            return
        if contents[count - 1].strip(" ") == "":
            print("Cannot add an empty string.")
            return
        
        profile.username = contents[count - 1]
        profile.save_profile(file)

    # -pwd [PASSWORD]
    if ' -pwd ' in text:
        change = True
        count += 2
        contents = text.split(quotes)
        if " " in contents[count - 1]:
            print('Password should not have whitespace!')
            return
        if contents[count - 1].strip(" ") == "":
            print("Cannot add an empty string.")
            return
        profile.password = contents[count - 1]
        profile.save_profile(file)

    # -bio [BIO]
    if ' -bio ' in text:
        change = True
        count += 2
        contents = text.split(quotes)
        if contents[count - 1].strip(" ") == "":
            print("Cannot add an empty string.")
            return
        profile.bio = contents[count - 1]
        profile.save_profile(file)

    # -addpost [NEW POST]
    if ' -addpost ' in text:
        change = True
        count += 2
        contents = text.split(quotes)
        if contents[count - 1].strip(" ") == "":
            print("Cannot add an empty string.")
            return
        post = Post()
        post.set_entry(contents[count - 1])
        profile.add_post(post)
        profile.save_profile(file)

    # -delpost [ID]
    if ' -delpost ' in text:
        change = True
        contents = text.strip("E -delpost ")
        index = int(contents)
        profile.del_post(index)
        profile.save_profile(file)
    
    if not change:
        print('Please enter a valid command.')


def create_file(dtry, name):
    """Create a file."""
    p = Path(dtry)
    p = p / name

    if not p.exists():
        p.touch()
    
    print(p)
    return p
