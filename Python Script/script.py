from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


url = "http://14.139.205.172/web_new/Default.aspx"
options = webdriver.ChromeOptions()
options.addargument('--headless')
driver = webdriver.Chrome(options=options)
driver.get(url)

##ASSIGNING VARIABLES TO TEXT BOX AND BUTTONS 
roll_box = driver.find_element_by_id("txtRegno")
sem_select = Select(driver.find_element_by_id("ddlSemester"))
show_result_button = driver.find_element_by_id("btnimgShowResult")

##GLOBAL DECLARATIONS FOR THE LISTS
roll_list = []
name_list = []
subjects_list = []
top_list = []
top_marks_list = []
failed_list = []



class get_data:
	def __init__(self, year, code, limit, semester):
		global driver
		global roll_box
		global sem_select
		global show_result_button

		roll_final = str(year)+name+str(limit)
		roll_box.clear()
		roll_box.send_keys(roll_final)
		roll_box.send_keys(Keys.ENTER)
		roll_box.select_by_value(str(semester))
		show_result_button.click()



