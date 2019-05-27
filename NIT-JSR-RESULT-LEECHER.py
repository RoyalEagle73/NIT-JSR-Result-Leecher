from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#LISTS AND DATA STRUCTURES TO BE USED
data_to_print = ""

print("*************** Welcoome To NIT JSR Result Leecher ***************")
print("For more work, find me @ Github.com/RoyalEagle73\n\n\n")

roll_no = input("Enter Roll Number without last digits :\n(For example enter 2018PGCACA if your class is of batch 2018 and MCA) :\n")       ## (YEAR CAN BE CHANGED ACCORDINGLY )


roll_no_int = int(input("Enter Initial Roll Number :\n"))


final_roll = int(input("Enter Last Roll Number of Class :\n"))


semester_count = int(input("Enter Number of semesters to count result for :\n"))

##OPENING URL
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get("http://14.139.205.172/web_new/Default.aspx")


temp_count = 1
while temp_count<semester_count+1:
	data_to_print += "SGPA(Sem %d),"%(temp_count)
	temp_count +=1
data_to_print += "Final CGPA\n"

result = []
roll_list = []

sum_marks = 0.0

while roll_no_int!=final_roll+1:			## ( LIMIT CAN BE PLACED HERE )
	roll_no_temp = roll_no
	##CHANGING ROLL NUMBER
	if roll_no_int<=9:
		roll_no_final = roll_no_temp + '0' + str(roll_no_int)
	else:
		roll_no_final = roll_no_temp + str(roll_no_int)

	print(roll_no_final + "'s Result being fetched")

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

	data_box.send_keys(roll_no_final)
	try:
		data_box.send_keys(Keys.ENTER)
		temp_count = 1
		while temp_count <= semester_count:
			try:
				sem_select = Select(driver.find_element_by_id("ddlSemester"))
				sem_select = Select(driver.find_element_by_id("ddlSemester"))
				try:
					sem_select.select_by_value(str(temp_count))
					enter_button = driver.find_element_by_id("btnimgShowResult")
					enter_button.click()

					if temp_count == 1:	
						sgpa =driver.find_element_by_id("lblCPI")
						name = driver.find_element_by_id("lblStudentName")
						#print(roll_no_int,name.text, sgpa.text, end=" ")
						data_to_print += "\n"+roll_no_final + "," +name.text+","+sgpa.text+","
					elif temp_count >1 and temp_count < semester_count:
						sgpa =driver.find_element_by_id("lblCPI")
						data_to_print += sgpa.text+","
						#print(sgpa.text, end=" ")
					elif temp_count == semester_count:
						sgpa =driver.find_element_by_id("lblCPI")
						cgpa = driver.find_element_by_id("lblSPI")
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
	
		
	roll_no_int += 1

driver.close()


file_name = roll_no_temp + ".xlsx"
data_to_print += "For more work, find me @ Github.com/RoyalEagle73\n"
with open(file_name, "w") as result:
	result.write(data_to_print)

print("Successfully generated file with name %s at script location..........")%(file_name)