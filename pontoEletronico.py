from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver", service_log_path="/dev/null")  

driver.get("https://web.manpowergroup.com.br/portal/")
driver.find_element(By.XPATH,"//*[@id='cookieConsentContainer']/div[3]/a").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/app-root/app-login-page/div/div[1]/div[2]/form/div[1]/p/input").send_keys("seuemail@outlook.com")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/app-root/app-login-page/div/div[1]/div[2]/form/div[2]/p/input").send_keys("suasenha")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/app-root/app-login-page/div/div[1]/div[2]/form/div[3]/div[2]").click()
time.sleep(4)
driver.get("https://web.manpowergroup.com.br/portal/ponto-eletronico")
time.sleep(2)
driver.find_element(By.CLASS_NAME,"delete").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/app-root/app-main-point/app-layout-in-portal/app-content-frame/div[1]/div/div/app-simple-point/div[3]/div/div[3]/button").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div/div/div[3]/button[1]").click()