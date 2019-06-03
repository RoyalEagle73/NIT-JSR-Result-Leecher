from tkinter import *
from tkinter import messagebox
from script import driver_program
import webbrowser

home = Tk()
home.title("NIT JSR RESULTS LEECHER")


#TITLE LABEL
title_label = Label(home, text = "*********** NIT JSR RESULTS LEECHER ***********", fg="red", bg="black")
title_label.place(x=55, y=10)

#CODE ENTRY lABEL
code_entry_label = Label(home, text="Enter Course Code ( As 'PGCACA' in 2018PGCACA63 ): ", bg="black", fg="purple")
code_entry_label.place(x = 20, y = 100)

#CODE ENTRY BOX
code_entry = Entry(home)
code_entry.configure(width=50)
code_entry.place(x=20, y=120)

#YEAR LABEL
year_label = Label(home, text = "Enter Your Batch Year (in Digits):", fg="purple", bg="black")
year_label.place(x=20, y=40)

#YEAR ENTRY BOX
year_entry = Entry(home)
year_entry.configure(width=50)
year_entry.place(x=20, y=60)

#SEMESTER ENTRY lABEL
sem_entry_label = Label(home, text="Enter number of Semesters to collect data for (in Digits): ", bg="black", fg="purple")
sem_entry_label.place(x = 20, y = 220)

#SEMESTER ENTRY BOX
sem_entry = Entry(home)
sem_entry.configure(width=50)
sem_entry.place(x=20, y=240)

#ROLL ENTRY lABEL
roll_entry_label = Label(home, text="Enter last roll number in batch (in Digits) : ", bg="black", fg="purple")
roll_entry_label.place(x = 20, y = 160)

#CODE ENTRY BOX
roll_entry = Entry(home)
roll_entry.configure(width=50)
roll_entry.place(x=20, y=180)

update_1_label = Label(home, text="Note:\nPlease wait for some moment after clicking above button\ntill next update appears.......", bg="black", fg="yellow")
update_1_label.place(x=33, y=340)


def drive(event):
	global year_entry
	global code_entry
	global roll_entry
	global sem_entry

	
	driver_program((year_entry.get()+code_entry.get()), int(roll_entry.get()), int(sem_entry.get()))

	update_2_label = Label(home, text="Update:\nResult has been saved \nwith name %s.csv in the same directory...."%(year_entry.get()+code_entry.get()), bg="black", fg="green")
	update_2_label.place(x=45, y=400)

def github_callback(event):
	webbrowser.open_new("https://Github.com/RoyalEagle73")

def facebook_callback(event):
	webbrowser.open_new("https://Facebook.com/RoyalEagle073")

def linkedin_callback(event):
	webbrowser.open_new("https://www.linkedin.com/in/deepak-chauhan-173756170/")

#MY INFO BUTTON	
my_info = Label(home, text = "Connect to me Here :", bg = "black", fg = "purple")
my_info.place(x=20, y=450 )

github = Label(home, text = "Github", fg= "orange", bg="black")
github.bind("<Button-1>",github_callback)
github.place(x=20, y=470)


facebook = Label(home, text = "Facebook", fg= "white", bg="black")
facebook.bind("<Button-1>", facebook_callback)
facebook.place(x=100, y=470)


linkedin= Label(home, text = "Linkedin", fg= "green", bg="black")
linkedin.bind("<Button-1>", linkedin_callback)
linkedin.place(x=180, y=470)

#Generate Button 
generate_button  = Button(home, text="GENERATE", bg="purple", fg="white")
generate_button.bind("<Button-1>", drive)
generate_button.place(x=145, y=290)


home.configure(background="black")
home.configure(height = 500, width=400)
home.resizable(0,0)
home.mainloop()