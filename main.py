from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://scraperwiki.com/")
element = driver.find_element_by_xpath('//*[@id="main"]/article/section/div[1]/div[3]/div/a')
element.click()
