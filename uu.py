import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.actitime.com/login.do")
time.sleep(3)
driver.find_element(By.NAME,"username").send_keys("admin")
driver.find_element(By.NAME,"pwd").send_keys("manager")
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Login").click()
time.sleep(4)

print("click on task tab")
driver.find_element(By.CSS_SELECTOR,"div[id=container_tasks").click()

print("click on add new Button")
time.sleep(4)
driver.find_element(By.XPATH,"//div[@class='addNewContainer']").click()

print("select the new customer menu")
time.sleep(3)

driver.find_element(By.XPATH,"//div[@class='item createNewCustomer']").click()

print("Enter the customer name")
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='customerNameDiv']/input[@placeholder='Enter Customer Name']").send_keys("CSK")

print("enter the customer descripation")
time.sleep(3)
driver.find_element(By.XPATH, "//textarea[@placeholder='Enter Customer Description']").send_keys("hdfc")
print("select customer dropdown")
time.sleep(3)
driver.find_element(By.XPATH, "//div[text()='- select Customer -']").click()
time.sleep(4)
driver.find_element(By.XPATH,"//div[@class='searchItemList']/div[text()='Big Bang Company']").click()
time.sleep(4)
driver.find_element(By.XPATH,"//div[@class='components_button withPlusIcon']").click()
time.sleep(7)
