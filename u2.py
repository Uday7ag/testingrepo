import pytest
import sys
import selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
def test_lambdatest_todo_app():
    chrome_driver=webdriver.Chrome()
    chrome_driver.get("'https://lambdatest.github.io/sample-todo-app/")
    chrome_driver.maximize_window()
    chrome_driver.find_element(By.NAME,"li1").click()
    chrome_driver.find_element(By.NAME,"li2").click()
    title="sample page-lambdatest.com"
    assert title==chrome_driver.title
    sample_text="one more check box"
    email_text_field=chrome_driver.find_element(By.ID,"sampletodotext")
    email_text_field.send_keys(sample_text)
    sleep(5)
    chrome_driver.find_element(By.ID,"addbutton").click()
    sleep(5)
    output_str=chrome_driver.find_element(By.NAME,"li6").text
    sys.stderr.write(output_str)