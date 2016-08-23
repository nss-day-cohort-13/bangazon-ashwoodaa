import os
import sys
import pickle
import time
import uuid
from user import *
from chirp import *

class Birdy_Board():

  users_filename = 'users.p'
  chirps_filename = 'chirps.p'

  def __init__(self):
    """
    Initialization

    """
    self.current_user = None
    self.current_chirp = None


    try:
      self.all_users = self.deserialize_data(self.users_filename)
    except EOFError:
      self.all_users = {}
    try:
      self.all_chirps = self.deserialize_data(self.chirps_filename)
    except EOFError:
      self.all_chirps = {}


  def page_clear(self):
    '''
    This clears the page

    '''
    #this gives issues with macs
    clear = lambda: os.system('cls')
    clear()

  def show_main_menu(self):
    '''
    Shows main menu and allows 'admin' to add chirps if current user

    '''
    while True:
      self.page_clear()
      if not self.current_user:
        print('No Current User')
      else:
        print('Current user: ', self.current_user.screen_name)
      print("""  *********************************************************
  **  Welcome to BirdyBoard!   **
  *********************************************************
  1. Create a User
  2. Select User
  3. Make a Chirp
  4. View Chirps
  5. Exit""")

      user_choice = input("Select an option: ").lower()
      # time.sleep(1)
      if user_choice == '1':
        self.create_user()
      elif user_choice == '2':
        self.select_user()
      elif user_choice == '3':
        if not self.current_user:
          print('Please create or select a user')
          time.sleep(1.5)
          continue
        else:
          self.create_chirp()
      elif user_choice == '4':
        if not self.current_user:
          print('Please create or select a user')
          time.sleep(1.5)
          continue
        else:
          self.list_chirps()
      elif user_choice == '5':
        sys.exit()
      elif user_choice == 'chirps':
        self.list_chirps()
        time.sleep(4)
      elif user_choice == 'users':
        self.list_users()
        time.sleep(4)

      else:
        print('Invalid Input')
        time.sleep(1)



  def create_user(self):
    self.page_clear()
    print("Let's create a user")

    full_name = input('Enter First and Last Name: ')
    screen_name = input('Screen Name: ')

    new_user = User(full_name, screen_name)

    self.current_user = new_user
    self.all_users[new_user.user_uuid] = new_user
    self.serialize_data(self.all_users, self.users_filename)
    time.sleep(1)


  def select_user(self):
    while True:
      self.page_clear()
      print('Select a User')
      if self.all_users == {}:
        print('No users exist, please create a new user')
        time.sleep(1.5)
        return #back to main menu
      else:
        user_line_to_uuid = self.list_users() # returns uuid {line_number: uuid}
        line_number = input("Select a User > ") # line_number = line selected
        if line_number not in user_line_to_uuid:
          print('Not a valid User')
          time.sleep(1)
        else:
          current_uuid = user_line_to_uuid.get(line_number) # get uuid from user_line_to_uuid
          self.current_user = self.all_users.get(current_uuid) # pass uuid from line = current user
          return #back to main menu


  def create_chirp(self):
    self.page_clear()
    print("What's on your mind?")
    time.sleep(.5)

    add_chirp = input('Enter Chirp Text: ')
    new_chirp = Chirp(add_chirp)
    self.all_chirps[new_chirp.chirp_uuid] = new_chirp
    print("Your chirp was created.")
    self.serialize_data(self.all_chirps, 'chirps.p')
    time.sleep(2)
    pass

  def list_users(self):
    line_count = 1
    user_line_to_uuid = {} #new dict to hold uuid
    for uuid, value in self.all_users.items():
      user_line_to_uuid[str(line_count)] = uuid
      print('{}.  {}'.format(line_count, value.screen_name))
      line_count += 1
    return user_line_to_uuid # to select_user

  def list_chirps(self):
    line_count = 1
    chirp_line_to_uuid = {} # new dict to hold uuid
    for uuid, value in self.all_chirps.items():
      chirp_line_to_uuid[str(line_count)] = uuid
      print('{}.  {}'.format(line_count, value.chirp_text))
      line_count += 1
    viewing_chirps_exit_option_input = input("\nType \'321\' to Exit: ")

    if viewing_chirps_exit_option_input == '321':
      #go back to menu thing would go here but in the mean time we have this
      sys.exit()
    elif viewing_chirps_exit_option_input != '321':
      print('Not a valid Choice')
      time.sleep(1.5)
    return chirp_line_to_uuid # to select_chirp


  def serialize_data(self, data, filename):
    # wb+ w/r in binday format
    with open(filename, 'wb+') as file:
      pickle.dump(data, file)


  def deserialize_data(self, filename):
    # filename
    # rb+ r/w in binary format
    try:
      with open(filename, 'rb+') as file:
        data = pickle.load(file)
    except FileNotFoundError:
      data = {}
    return data



if __name__ == '__main__':
  birdy_board = Birdy_Board()
  birdy_board.show_main_menu()
