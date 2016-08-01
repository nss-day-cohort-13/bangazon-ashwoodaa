#here is where I need to put my imports

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
    print("""\n\n*********************\nYou chose to create a new user.\n*********************\n
    \n\n Enter Full Name:
    \n\n Enter Screen Name: """) #This needs to have inputs
  elif selection == '2':
    print("""\n\n*********************\nYou chose to view Chirps.\n*********************\n
      \n\n Here are the Chirps: """) #list public and private chirps
  elif selection == '3':
    print("""\n\n*********************\nWrite a public Chirp.\n*********************\n
      \n\n Which User is Chirping?
      #here is where we would list the registered users
      \n\nMake your selection: """) #here we would have a options input thing for users
  elif selection == '4':
    print("""\n\n*********************\nWrite a private Chirp.\n*********************\n
      \n\n Chirp at
      \n #here we would list possible ppl you can chirp at
      \n\nEnter your private chirp: #here is where the input text field would be
      \n\n Cancel Option #here is where we would have a cancel option""")
  elif selection == '5':
    break
  else:
    print("Unknown Option Selected!")
    #this takes care of faulty inputs