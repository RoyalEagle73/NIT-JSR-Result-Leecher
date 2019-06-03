from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import datetime
# from tkinter import *
# from tkinter.ttk import *
# import threading

class result:
	def __init__(self,roll_no, final_roll):
		# self.home = Tk()
		# self.progress = Progressbar(self.home, orient=HORIZONTAL,length=200, mode='determinate')
		self.roll_no  = roll_no
		self.final_roll = final_roll 
		self.year = int(self.roll_no[:4])
		
		this_time = datetime.now()
		if(this_time.month >= 1 and this_time.month<=7):
			self.semester_count =  ( this_time.year - self.year - 1)*2 + 2
		elif(this_time.month >= 8 or this_time.month<=12):
		 	self.semester_count =  ( this_time.year - self.year)*2 + 1

		
	# def bar(self, roll):
	# 	percent = (roll / self.final_roll)*100
	# 	self.progress['value'] = percent
	# 	self.home.update_idletasks()
	# 	print(percent)
	# 	print("being called")

	def driver_fun(self):
		this_time = datetime.now()

		if self.year > this_time.year :
			messagebox.showerror("Error", "Please Enter Correct Year in Roll Number")
			return
		
		messagebox.showinfo("UPADTE-1","1) Extraction has been started, please     wait till next pop-up appears.\n2) Application may appear dead as it     works in background.")

		data_to_print = "Roll No,   Name,"

		options = webdriver.ChromeOptions()
		options.add_argument('--headless')
		driver = webdriver.Chrome(options=options)
		driver.get("http://14.139.205.172/web_new/Default.aspx")
		
		temp_count = 1
		while temp_count<self.semester_count+1:
			data_to_print += "   SGPA(Sem %d),"%(temp_count)
			temp_count +=1
		data_to_print += "Final CGPA"

		self.roll_no_int = 1
		while self.roll_no_int!=self.final_roll+1:
			# x = threading.Thread(target=self.bar, args=(self.roll_no_int,))			
			# x.start()
  
			self.roll_no_temp = self.roll_no
			##CHANGING ROLL NUMBER
			zero = ""
			after_ten = ""

			if self.final_roll >= 100:
				zero = "00"
				after_ten = "0"
			else:
				zero = "0"
				after_ten = ""

			if self.roll_no_int<=9:
				self.roll_no_final = self.roll_no_temp + zero + str(self.roll_no_int)
			else:
				self.roll_no_final = self.roll_no_temp + after_ten +str(self.roll_no_int)

			print(self.roll_no_final + "'s Result being fetched")

			##GETTING RESULT
			try:
				data_box = driver.find_element_by_id("txtRegno")
				data_box.clear()
			except Exception as e:
				driver.close()
				options = webdriver.ChromeOptions()
				options.add_argument('--headless')
				driver = webdriver.Chrome(options=options)
				driver.get("http://14.139.205.172/web_new/Default.aspx")
				data_box = driver.find_element_by_id("txtRegno")
				data_box.clear()

			data_box.send_keys(self.roll_no_final)
			try:
				data_box.send_keys(Keys.ENTER)
				temp_count = 1
				while temp_count <= self.semester_count:
					try:
						sem_select = Select(driver.find_element_by_id("ddlSemester"))
						sem_select = Select(driver.find_element_by_id("ddlSemester"))
						try:
							sem_select.select_by_value(str(temp_count))
							enter_button = driver.find_element_by_id("btnimgShowResult")
							enter_button.click()

							if temp_count == 1:	
								sgpa =driver.find_element_by_id("lblSPI")
								name = driver.find_element_by_id("lblStudentName")
								#print(self.roll_no_int,name.text, sgpa.text, end=" ")
								data_to_print += "\n"+self.roll_no_final + "," +name.text+","+sgpa.text+","
							elif temp_count >1 and temp_count < self.semester_count:
								sgpa =driver.find_element_by_id("lblSPI")
								data_to_print += sgpa.text+","
								#print(sgpa.text, end=" ")
							elif temp_count == self.semester_count:
								sgpa =driver.find_element_by_id("lblSPI")
								cgpa = driver.find_element_by_id("lblCPI")
								data_to_print += sgpa.text+","+cgpa.text

							temp_count += 1
			
						except Exception as e:
							temp_count += 1	
					except Exception as e:
						temp_count += 1	
			except Exception as e:
				## EXCEPTION DOES'NT COUNT ABSENT ROLL
				pop_up = driver.switch_to.alert
				pop_up.accept()
			
				
			self.roll_no_int += 1

		driver.close()
		file_name = self.roll_no_temp + ".csv"
		data_to_print += "\nFor more work:, find me @ Github.com/RoyalEagle73\n"
		with open(file_name, "w") as result:
			result.write(data_to_print)

		messagebox.showinfo("UPADTE-2", "1) Data has been extracted and can be found in same directory as application.\n2) File saved with name - %s.\n3) Application will automatically after you click OK."%(file_name))

		quit()
