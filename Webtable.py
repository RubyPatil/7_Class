from selenium import webdriver

driver=webdriver.Chrome()
driver.get("file:///C:/Users/Dell/Desktop/webtable2.html")
driver.maximize_window()
driver.implicitly_wait(30)

#ele=driver.find_elements_by_xpath("//*[@id='emp']/thead/tr/th")
ele=driver.find_elements_by_xpath("//*[@id='emp']/tbody/tr[1]/td") # For first row length

print(len(ele))

first_part="//*[@id='emp']/thead/tr/th["
second_part="]"
driver.close()
