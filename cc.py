import time


from selenium import webdriver
from selenium.webdriver.common.by import By

print("open the browser")
driver=webdriver.Chrome()
driver.maximize_window()

print("enter the URL")
driver.get("https://demo.actitime.com/")

print("login to the application")
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.NAME,"pwd").send_keys("manager")
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Login").click()
time.sleep(3)

print("click on task tab")
driver.find_element(By.CSS_SELECTOR,"div[id=container_tasks]").click()

print("click on add new Button")
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='addNewContainer']").click()

print("selet the new customer menu")
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='item createNewCustomer']").click()

print("Enter the customer name")
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div[51]/div/div[2]/div[1]/div/div[1]/div[1]/input").send_keys('xyz')

print("enter the customer description")
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div[51]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/textarea").send_keys("Banking Project")

print("select customer dropdown")
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='comboboxButton']//div[@class='dropdownButton']").click()

print("select our company in the dropdown")
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div[51]/div/div[2]/div[1]/div/div[1]/div[3]/div[2]/span/div/div[2]/div/div[1]/div/div[6]").click()

print("click on create customer")
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='components_button withPlusIcon']").click()

print("customer company succesfully created")

print("logout from the application")
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Logout").click()
time.sleep(10)

print("close the Browser")
driver.close()