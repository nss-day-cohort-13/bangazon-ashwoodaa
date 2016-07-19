# Birdyboard
## Command Line Message Board

In this app, users will create and read public and private messages via terminal input.

## Instructions

Create a series of prompts for users to create and reply to messages in a twitter/message board hybrid.

### Main Menu
```bash
#########################################
##           Birdyboard~~~~~           ##
#########################################
1. New User Account
2. Select User
3. View Chirps
4. Public Chirp
5. Private Chirp
6. Exit
>
```


### New User
```bash
Enter full name
>

Enter screen name
>
```


### Select User
```bash
Which user is chriping?
1. Tweedleedee
2. BiffBoffin
...
>
```


### View Chirps
Chirps are separated into public and private chirps.  Only the two users involved in a private chirp can see it in their Private Chirps section.
```bash
<< Private Chirps >>
1. BiffBoffin: Hey, you up for ping...
2. Lara_keet: Any idea what Jeff wa...
3. BiffBoffin: Hah, you got wrecked...
<< Public Chirps >>
4. Tweedleedee: Anybody know a good...
5. Fuzzy: Do NOT try the mega ultra...
6. Velton32: You guys have got to s...
...
9. Main Menu
>
```

Selecting an individual chirp takes you to that chirp's comment thread.
```bash
Tweedleedee: Anybody know a good Thai restaraunt in the area?
Fuzzy: Smiling Elephant is really good
BiffBoffin: The pad krapow is amazing!
...
1. Reply
2. Back
>
```


### New Chirp
Users can chirp publicly or they can start a private chirp with another user.

#### Public
```bash
Enter chirp text
>
```

#### Private
```bash
Chirp at
1. BiffBoffin
2. Lara_keet
...
9. Cancel
>

Enter chirp text
>
```


# Requirements

1. A full test suite with full coverage of all methods
2. User data will be stored in a text file and should contain at minimum
  - A user ID number
  - Screen name
  - Full name
3. Chirps will be stored in a text file and should contain at minimum
  - A chirp ID number
  - Who authored the chirp
  - Is this a public or private chirp
  - Who the chirp is to (if applicable)
  - The text content of the chirp

### Challenge
[Serialize](https://docs.python.org/3.3/library/pickle.html) the user and chirp data before storage & deserialize on read.

# References

## How to get started

1. Tests first!
1. You can use `input()` and `print()` to show prompts and read user input.
1. You know how to use [`open()`, `readline()` and `write()`](https://docs.python.org/3.3/tutorial/inputoutput.html#reading-and-writing-files) to maniuplate data in text files.
1. You've worked with [CSV](https://docs.python.org/3.3/library/csv.html) files for data storage.
1. You can write conditional logic with `if`

Start with the basics

1. Show the main menu and read the user's choice with an `input()`.
1. Based on the user's choice, `print()` their choice, i.e. "You chose to make a new chirp."
1. Create the logic for each of the conditions to recieve further user input & display other menus.
1. Once all user input is received, perform the appropriate file action (reading from or writing to the chirps file), and direct the user back to the appropriate menu.
