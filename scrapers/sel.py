from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://myanimelist.net/topanime.php?limit=0')

element = driver.find_element_by_id('#area32281')
print element
