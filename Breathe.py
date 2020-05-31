#import modules

from tkinter import *
import os

# 4 Features

#Loading Screen Function Code
def loading_screen():
  import time
  time.sleep(1)
  print("Loading.")
  time.sleep(1)
  print("Loading..")
  time.sleep(1)
  print("Loading...")
  print (" ")

#Home Page
def home():
  import time
  print ("What would you like to do?")
  time.sleep(1)
  print ("m: Go climb your mountain (track progress)")
  time.sleep(1)
  print ("j: Reflect and journal")
  time.sleep(1)
  print ("r: Access resources")
  time.sleep(1)
  print ("z: Find some zen (meditate)")
  time.sleep(1)
  print ("e: Exit or remain on homepage!")
  time.sleep(1)
  home_selection = input("Enter 'j', 'm', 'r', 'z', or 'e': ")
  while home_selection.isalpha() != True:
    import time
    time.sleep(1)
    print("That was not a valid entry, please try again!")
    time.sleep(1)
    home_selection = input("Enter a \"j\" to access additional resources, \"m\" to go climb your mountain, \"r\" to reflect, \"z\" to find some zen, or \"e\" to quit: ")
  else:
    if home_selection.lower() == "m":
      loading_screen()
      import time
      time.sleep(1)
      print("Welcome to the Mountain Base!")
      time.sleep(1)
      print("Here we will show you an example of how we record your progress.")
      time.sleep(1)
      import matplotlib.pyplot as plt
      plot()
      home()
    elif home_selection.lower() == "j":  ##REFLECTION/JOURNAL
      loading_screen()
      import time
      print("Welcome to the Reflection Section!!")
      time.sleep(1)
      import datetime
      import os
      controls()
      home()
    elif home_selection.lower() == "z":
      loading_screen()
      import time
      time.sleep(1)
      print("Welcome to the Zen Den!")
      time.sleep(1)
      countdown()
      home()
    elif home_selection.lower() == "r":
      loading_screen()
      import time
      time.sleep(1)
      print("Here are some resources you can access to further your self care journey!")
      time.sleep(1)
      print("Kids Help Phone: Text 'CONNECT' to 686868 ")
      print("Crisis Services Canada: 1 (833) 456-4566 (Toll Free) ")
      print("Canadian Crisis Hotline: 1 (888) 353-2273 ")
      home()
    elif home_selection.lower() == "e":
      loading_screen()
      import time
      time.sleep(1)
      print("Staying at home!")
      time.sleep(1)
      home()
    else:
      import time
      time.sleep(1)
      print("That was not a valid entry, please try again!")
      time.sleep(1)
      home()

### Journal Functions

def journal_content():
    content = input("Write until your heart's content :) ") #user's journal/reflection entry
    return content

def add_content():
    import datetime 
    import time
    time.sleep(1)
    title = input("What's the title of your entry?  ") #get the title of entry
    content = journal_content() #content of entry
    filename = title.replace(" ","") + ".txt" #remove spaces in name 
    entry = open(filename, "a") #creates text file on desktop
    entry.write("Entry Title: " + title + "\n") #addg user's chosen title
    entry.write("Date: " + str(datetime.datetime.now()) + "\n") #adds the date
    entry.write("Entry: " + content + "\n")
    entry.close()

def controls():
    import time
    time.sleep(1)
    print("Would you like to create an entry? Type '1' to start. ")
    option = input ("Your choice:  ")
    time.sleep(1)
    print("-----\n-----")
    #pulls the content function so users can type out entry: 
    if option == "1" or option == 1:
        add_content()
    else:
        import time
        time.sleep(1)
        print("Please enter a valid response.")
        controls()
    #asks users if they need anything else
    time.sleep(1)
    choice = input("Would you like to add another entry? (y/n)")
    if choice == "y" or choice == "yes":
        import time
        time.sleep(1)
        controls()
    else:
        import time
        time.sleep(1)
        print("See you soon!")
        print("")
    #Asks if the user wants to do anything else. If not, program ends

##COUNTDOWN FEATURE

def countdown():
  import time 
  while True:
    
    #asks user if they want to meditate
    time.sleep(1)
    meditate = input (" Do you want to meditate? (y/n) ")

    #if user inputs "y" or "yes" then the user can input the time they want to meditate for
    time.sleep(1)
    if meditate.lower() == "y" or meditate.lower() == "yes":

    #asks user how many minutes they want to meditate for 
      uin = input ("How many minutes do you want to meditate for? ")
      try: 
            time.sleep(1)
            when_to_stop = abs(int(uin))*60
      
      except KeyboardInterrupt:
              break 
      except: 
              print ("Not a number!")

      while when_to_stop > -1:
              m, s = divmod(when_to_stop, 60)
              h, m = divmod(m, 60)
              time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
              print ("\r", end=time_left)
              time.sleep(1)
              when_to_stop -= 1

    #if user inputs anything besides "y" or "yes" then user is recommended to head back to homepage 
    else:
      import time
      time.sleep(1)
      print ("Head back to the homepage to check out some other calming activities!")
      break 

##GRAPHING FEATURE
# import plotting module 
import matplotlib.pyplot as plt

def plot ():
  import time
  print("Please choose a goal from the following list you would like to focus on:")
  time.sleep(1)
  print("Enter 1 to focus on self compassion")
  time.sleep(1)
  print("Enter 2 to focus on sleeping better")
  time.sleep(1)
  print("Enter 3 to focus on reducing stress")
  time.sleep(1)
  print("Enter 4 to focus on attaining a more balanced lifestyle")
  time.sleep(1)
  goals = input("Choose a goal you would like to develop: ")
  while goals <= "4":
      if goals == "1":
        #asking for user info everyday
        day1 = input ("Day 1: How happy do with you feel with yourself today from a scale of 1 - 5? ")
        day2 = input ("Day 2: How happy did you feel with yourself yesterday from a scale of 1 - 5? ")
        day3 = input ("Day 3: How happy did you feel with yourself two days ago from a scale of 1 - 5? ")
        # assigning x-axis values (each day past)
        x = [1,2,3] 
        # corresponding y axis values (feeling level inputs from user)
        y = [day1,day2,day3] 

        # plotting the points on graph
        plt.plot(x, y) 

        # naming the x axis 
        plt.xlabel('Last Three Days') 
        # naming the y axis 
        plt.ylabel('Self Compassion') 

        # giving a title to the graph 
        plt.title('My Progress Chart') 

        # function to show the plot 
        plt.show()
        break
      elif goals == "2":
        #asking for user info everyday
        import time
        day1 = input ("Day 1: How well did you sleep last night on a scale of 1 - 5? ")
        day2 = input ("Day 2: How well did you sleep the night before on a scale of 1 - 5? ")
        day3 = input ("Day 3: How well did you sleep the night before that on a scale of 1 - 5? ")
        time.sleep(1)
        # assigning x-axis values (each day past)
        x = [1,2,3] 
        # corresponding y axis values (feeling level inputs from user)
        y = [day1,day2,day3] 

        # plotting the points on graph
        plt.plot(x, y) 

        # naming the x axis 
        plt.xlabel('Last Three Days') 
        # naming the y axis 
        plt.ylabel('Sleeping Better') 

        # giving a title to the graph 
        plt.title('My Progress Chart') 

        # function to show the plot 
        plt.show()
        break

      elif goals == "3":
        #asking for user info everyday
        import time
        time.sleep(1)
        day1 = input ("Day 1: How stressed are you feeling today from a scale of 1 - 5? ")
        day2 = input ("Day 2: How stressed were you feeling yesterday from a scale of 1 - 5? ")
        day3 = input ("Day 3: How stressed were you feeling two days ago from a scale of 1 - 5? ")
        time.sleep(1)
        # assigning x-axis values (each day past)
        x = [1,2,3] 
        # corresponding y axis values (feeling level inputs from user)
        y = [day1,day2,day3] 

        # plotting the points on graph
        plt.plot(x, y) 

        # naming the x axis 
        plt.xlabel('Last Three Days') 
        # naming the y axis 
        plt.ylabel('Stress Level') 

        # giving a title to the graph 
        plt.title('My Progress Chart') 

        # function to show the plot 
        plt.show() 
        break
      elif goals == "4":
        #asking for user info everyday
        import time
        day1 = input ("Day 1: How crazy did your plans feel today from a scale of 1 - 5? ")
        day2 = input ("Day 2: How crazy did your plans feel yesterday from a scale of 1 - 5? ")
        day3 = input ("Day 3: How crazy did your plans feel two days ago from a scale of 1 - 5? ")
        time.sleep(1)
        # assigning x-axis values (each day past)
        x = [1,2,3] 
        # corresponding y axis values (feeling level inputs from user)
        y = [day1,day2,day3] 

        # plotting the points on graph
        plt.plot(x, y) 

        # naming the x axis 
        plt.xlabel('Last Three Days') 
        # naming the y axis 
        plt.ylabel('Balanced Life') 

        # giving a title to the graph 
        plt.title('My Progress Chart') 

        # function to show the plot 
        plt.show() 
        print("Here is how your how your progress has looked in reference to the last few days.")
        break
      else:
        print("Invalid entry")
        goals = input("Choose a goal you would like to develop: ")
  else:
    import time
    time.sleep(1)
    print("Invalid entry. Please try again.")
    while goals != goals.isdigit():
      import time
      time.sleep(1)
      goals = input("Choose a goal you would like to develop: ")
    else:
      import time
      time.sleep(1)
      home()
  
  print("This is an example of how your growth will be collected and displayed on a weekly basis!")



# Calling 4 Features

def progress():
      loading_screen()
      import time
      time.sleep(1)
      print("Welcome to the Mountain Base!")
      time.sleep(1)
      print("Here we will show you an example of how we record your progress.")
      time.sleep(1)
      import matplotlib.pyplot as plt
      plot()
      home()

def reflect():
      loading_screen()
      import time
      print("Welcome to the Reflection Section!!")
      time.sleep(1)
      import datetime
      import os
      controls()
      home()

def meditate():
      loading_screen()
      import time
      time.sleep(1)
      print("Welcome to the Zen Den!")
      time.sleep(1)
      countdown()
      home()

def resources():
      loading_screen()
      import time
      time.sleep(1)
      print("Here are some resources you can access to further your self care journey!")
      time.sleep(1)
      print("Kids Help Phone: Text 'CONNECT' to 686868 ")
      print("Crisis Services Canada: 1 (833) 456-4566 (Toll Free) ")
      print("Canadian Crisis Hotline: 1 (888) 353-2273 ")
      home()

# Designing window for registration
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="dark turquoise").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="dark turquoise", command = register_user).pack()


# Designing window for login 

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

# Implementing event on register button

def register_user():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration successful. Please go to the login page.", fg="dark turquoise", font=("calibri", 11)).pack()

# Implementing event on login button 

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()

# Designing popup for login success

def login_sucess():

    global breathe_screen
    breathe_screen = Tk()
    breathe_screen.geometry("350x300")
    breathe_screen.title("Login Successful")
    Label(breathe_screen, text="Welcome to Breathe! What would you like to do?").pack()
    Button(breathe_screen, text="Journal", command=reflect).pack()
    Label(text="").pack()
    Button(breathe_screen, text="Meditate", command=meditate).pack()
    Label(text="").pack()
    Button(breathe_screen, text="Track Progress", command=progress).pack()
    Label(text="").pack()
    Button(breathe_screen, text="Resources", command=resources).pack()
    Label(text="").pack()

    main_screen.mainloop()

# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Deleting popups

def delete_breathe_screen():
    breathe_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("400x250")
    main_screen.title("Account Login")
    Label(text="Welcome to the Breathe Community! Select Your Choice.", bg="dark turquoise", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()
