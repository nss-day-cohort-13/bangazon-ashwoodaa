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
    # print("\n\nEnter your Full Name and Screen Name separated by a comma")
    full_name=input("\n\n Enter Full Name: ")
    screen_name=input("\n\n Enter Screen Name: ")
    user_dictionary={} #here I declare the dictionary to store the user info that we are going to be putting in a list
    user_dictionary['full_name']=full_name
    user_dictionary['screen_name']=screen_name
    users_list_of_dictionaries.append(user_dictionary)
    print("users_list_of_dictionaries" + str(users_list_of_dictionaries))
    print("user_dictionary" + str(user_dictionary)) #printing this just to test it
    print("\n***************************************")
    print("\nYour Full Name is " + full_name + ".")
    print("\nYour Screen Name is " + screen_name + ".")
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