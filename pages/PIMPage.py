from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class PIMpage :
    #locators
    #add employee
    button_menuPIM_Xpath = (By.XPATH,"//span[normalize-space() = 'PIM']")
    button_addemployee_Xpath = (By.XPATH, "//a[normalize-space()='Add Employee']")
    txtfirstname_Xpath = (By.XPATH, "//input[@placeholder='First Name']")
    txtmiddlename_Xpath = (By.XPATH, "//input[@placeholder='Middle Name']")
    txtlastname_Xpath = (By.XPATH, "//input[@placeholder='Last Name']")
    txtemployeeid_Xpath = (By.XPATH,"//label[text()='Employee Id']/following::input[1]")
    button_save_Xpath = (By.XPATH,  "//button[normalize-space()='Save']")
    toaster_Xpath = (By.XPATH, "//div[@id='oxd-toaster_1']")

    #personal details_heading
    personaldetails_heading_Xpath = (By.XPATH, "//div[@class='orangehrm-edit-employee-name']//h6")

    #Table data records
    button_employee_list_Xpath = (By.XPATH,"//a[normalize-space()='Employee List']")
    table_rows_Xpath = (By.XPATH,"//div[@class='oxd-table-card']")
    button_nextpage_Xpath = (By.XPATH, "//i[contains(@class,'bi-chevron-right')]/parent::button")


    #constructor
    def __init__(self, driver):
        self.driver =driver
        self.wait = WebDriverWait(driver, 20)
    
    #Actions
    def clickPIMbutton(self):
        self.wait.until(EC.element_to_be_clickable(self.button_menuPIM_Xpath)).click()
    
    def clickAddEmployeebutton(self):
        self.wait.until(EC.element_to_be_clickable(self.button_addemployee_Xpath)).click()
    
    def add_employee_details(self, firstname, middlename, lastname, employeeid):
        time.sleep(5)
        self.fname =self.wait.until(EC.visibility_of_element_located(self.txtfirstname_Xpath))
        self.fname.send_keys(firstname)
        self.mname =self.wait.until(EC.visibility_of_element_located(self.txtmiddlename_Xpath))
        self.mname.send_keys(middlename)
        self.lname =self.wait.until(EC.visibility_of_element_located(self.txtlastname_Xpath))
        self.lname.send_keys(lastname)
        self.empid =self.wait.until(EC.visibility_of_element_located(self.txtemployeeid_Xpath))
        self.empid.click()
        self.empid.send_keys(Keys.CONTROL + "a")
        self.empid.send_keys(Keys.DELETE)
        self.empid.send_keys(employeeid)

    def clicksave_button(self):
        self.wait.until(EC.element_to_be_clickable(self.button_save_Xpath)).click()

    def verify_toaster(self):
        self.toaster= self.wait.until(EC.visibility_of_element_located(self.toaster_Xpath))
        return self.toaster.text
    def wait_for_toaster_disappear(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.toaster_Xpath))
        except:
            pass
    
    def get_personal_details_heading(self):
        self.heading = self.wait.until(EC.visibility_of_element_located(self.personaldetails_heading_Xpath))
        return self.heading.text
    
    def get_firstname(self):
        self.field = self.wait.until(EC.visibility_of_element_located(self.txtfirstname_Xpath))
        return self.field.get_attribute("value")
    
    def get_middlename(self):
        self.field = self.wait.until(EC.visibility_of_element_located(self.txtmiddlename_Xpath))
        return self.field.get_attribute("value")

    def get_lastname(self):
        self.field = self.wait.until(EC.visibility_of_element_located(self.txtlastname_Xpath))
        return self.field.get_attribute("value")

    def get_employeeid(self):
        self.field = self.wait.until(EC.visibility_of_element_located(self.txtemployeeid_Xpath))
        return self.field.get_attribute("value")
    
    def click_employee_list(self):
        self.employeelist = self.wait.until(EC.element_to_be_clickable(self.button_employee_list_Xpath))
        self.employeelist.click()

    def get_currentpage_records(self):

        self.all_records = []

        self.rows = self.wait.until(EC.visibility_of_all_elements_located(self.table_rows_Xpath))

        for self.row in self.rows:
            self.cells = self.driver.find_elements(By.XPATH, ".//div[@role='cell']")
            self.row_data = [self.cell.text.strip() for self.cell in self.cells]
            self.all_records.append(self.row_data)
        return self.all_records
    
    def click_next_page(self):
        try:
            self.next_button = self.wait.until(EC.element_to_be_clickable(self.button_nextpage_Xpath))

            if self.next_button.is_enabled() and "disabled" not in self.next_button.get_attribute("class"):
                self.next_button.click()
                return True
            return False
        except:
            return False
    
    def is_record_present(self, search_value):
        self.page_number = 1
        while True:
            print(f"searching in page : {self.page_number}")
            self.records = self.get_currentpage_records()

            for self.record in self.records:
                if search_value in  self.record:
                    print(f"{search_value} in page number {self.page_number}")
                    return True
            if self.click_next_page():
                self.page_number +=1
            else:
                print(f"{search_value}, valus is not found in the table")
                return False
        # print(f"{search_value} not found in any page ")