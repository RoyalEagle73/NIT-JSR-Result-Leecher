from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import script
import webbrowser

home = Tk()
home.title("NIT JSR Result Leecher")

fb = ImageTk.PhotoImage(Image.open("fb.png"))
github_img = ImageTk.PhotoImage(Image.open("github.png"))
linkedin_img = ImageTk.PhotoImage(Image.open("linkedin.png"))
nit = ImageTk.PhotoImage(Image.open("nit.png"))

logo = Label(home, image=nit)
logo.place(x=140, y=5)

title_label = Label(home, text="Welcome to NIT Jamshed Pur", bg="black", fg="teal")
title_label.configure(font=("Times New roman", 16, "bold"))
title_label.place(x=80, y=140)

title2_label = Label(home, text="*** Results Leecher ***", bg="black", fg="orange")
title2_label.configure(font=("Monotype Corsiva", 12, "italic"))
title2_label.place(x=115, y=160)


##### ROLL ENTRY AND LABEL
roll_label = Label(home,text="STEP 1 :\nEnter Last Roll Number In Your Class\n( e.g. 2018PGCACA87 )", fg="pink", bg ="black")
roll_label.place(x=90, y=200)

roll_entry = Entry(home, fg="saddle brown", bg="azure")
roll_entry.configure(width = 40)
roll_entry.place(x=50, y=250)

##NOTE LABEL
note = Label(home, text="NOTE:\n1) Application may appear dead while functioning.\n2) This is just a button not punching bag, so click it only once.", fg="firebrick1", bg="black")
note.place(x=17, y=370)


##### ROLL CALCULATION AND FUNCTIONS
def github_callback(event):
	webbrowser.open_new("https://Github.com/RoyalEagle73")

def facebook_callback(event):
	webbrowser.open_new("https://Facebook.com/RoyalEagle073")

def linkedin_callback(event):
	webbrowser.open_new("https://www.linkedin.com/in/deepak-chauhan-173756170/")

def work(event):
	global roll_entry
	global note 

	note.place_forget()
	home.update_idletasks()
	note = Label(home, text="Work Started Please Wait", fg="firebrick1", bg="black")
	note.place(x=17, y=370)
	home.update_idletasks()


	roll_code = ""
	last_roll = ""
	roll = roll_entry.get()
	index = 0
	for i in range(5, len(roll)):
		if roll[i].isdigit():
			index = i
			break
	roll_code = roll[:index]
	last_roll = roll[index:]

	if roll_code == "":
		messagebox.showerror("Error", "Please Enter Roll Number before you proceed")
		note.place_forget()
		home.update_idletasks()
		note = Label(home, text="Empty Fields", fg="firebrick1", bg="black")
		note.place(x=17, y=370)
		home.update_idletasks()

		return
	else:
		fun_object = script.result(roll_code, int(last_roll))
		fun_object.driver_fun()

		note.place_forget()
		home.update_idletasks()
		note = Label(home, text="Work Done", fg="firebrick1", bg="black")
		note.place(x=17, y=370)
		home.update_idletasks()

#### PROCEED BUTTON
proceed_Label = Label(home, text ="STEP 2:\nSmash the Button" ,fg="pink", bg ="black" )
proceed_Label.place(x=135, y=290)

proceed_button = Button(home, text="EXTRACT", bg="light goldenrod", fg="midnight blue")
proceed_button.bind("<Button-1>", work)
proceed_button.place(x=147, y=330)

##ABOUT ME TABS
about_me = Label(home, text = "-------------------- Follow me on -------------------- ", bg="black", fg="lime green")
about_me.configure(font=("Times New Roman", 15, "bold italic"))
about_me.place(x=40, y=430)

github = Label(home, image = github_img, bg="black")
github.bind("<Button-1>",github_callback)
github.place(x=80, y=470)


facebook = Label(home, image = fb, bg="black")
facebook.bind("<Button-1>", facebook_callback)
facebook.place(x=160, y=470)


linkedin= Label(home, image = linkedin_img, bg="black")
linkedin.bind("<Button-1>", linkedin_callback)
linkedin.place(x=240, y=470)

home.configure(background="black")
home.configure(height=550, width =400)
home.resizable(0,0)
home.mainloop()
