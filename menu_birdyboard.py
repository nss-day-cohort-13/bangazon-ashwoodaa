#here is where I need to put my imports
#just not sure which ones yet... it's cool. I'll figure it out after a little bit

#making my list of dictionaries to hold Users
users_list_of_dictionaries=[]


while True:
  print("""
 \n*******************************************
*   Welcome to BirdyBoard:                *
  \n*   1. New User Account                   *
  \n*   2. View Chirps                        *
  \n*   3. Public Chirp                       *
  \n*   4. Private Chirp                      *
  \n*   5. Exit                               *
  \n*******************************************
  """)

  selection = input("\n\nWhat would you like to do?: ")
  if selection =='1':
    print("\n\n*******************************\nYou chose to create a new user.\n*******************************\n")
    #get full name from user and store it in a variable
    full_name=input("\n\n Enter Full Name: ")
    #get screen name from user and store it in a variable
    screen_name=input("\n\n Enter Screen Name: ")
    #declare dictionary that will store user info and will be appended to users_list_of_dictionaries
    user_dictionary={}
    #adding full name to dictionary with the key being 'full_name'
    user_dictionary['full_name']=full_name
    #adding screen name to dictionary with the key being 'screen_name'
    user_dictionary['screen_name']=screen_name
    #appending the newly made user as a dictionary to the users_list_of_dictionaries
    users_list_of_dictionaries.append(user_dictionary)
    print("\n***************************************")
    print("\n --USER PROFILE--")
    print("\nYour Full Name is " + full_name + ".")
    print("\nYour Screen Name is " + screen_name + ".")
    print("\n***************************************")
    print("\n***************************************")
    print("\n --PRINTING TESTS--")
    #test printing user dictionary
    print("\ntest printing user_dictionary:  " + str(user_dictionary))
    #test printing the users_list_of_dictionaries to make sure it is storing everything
    print("\ntest printing users_list_of_dictionaries:  " + str(users_list_of_dictionaries))
    print("\n***************************************")


  elif selection == '2':
    print("""\n\n*******************************\nYou chose to view Chirps.\n*******************************\n
      \n\n Here are the Chirps: """) #list public and private chirps
  elif selection == '3':
    print("""\n\n*******************************\nWrite a public Chirp.\n*******************************\n
      \n\n Which User is Chirping?
      #here is where we would list the registered users
      \n\nMake your selection: """) #here we would have an options input thing for users
  elif selection == '4':
    print("""\n\n*******************************\nWrite a private Chirp.\n*******************************\nx
      \n\n Chirp at
      \n #here we would list possible ppl you can chirp at
      \n\nEnter your private chirp: #here is where the input text field would be
      \n\n Cancel Option #here is where we would have a cancel option""")
  elif selection == '5':
    break
  else:
    print("Unknown Option Selected!")
    #this takes care of faulty inputs