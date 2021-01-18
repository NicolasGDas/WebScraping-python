from selenium import webdriver
import xlsxwriter
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
f = open(r"C:\Users\nicog\OneDrive\Escritorio\Credenciales.txt","r")
driver = webdriver.Chrome(executable_path=r"D:\Selenium\chromedriver.exe")
driver.get(f.readline())
#Log in, lectura de credenciales
mail = f.readline()
contra = f.readline()
#limpio el campo
username = driver.find_element_by_id("email")
username.clear()
#mando el mail
username.send_keys(mail)
#limpio pass
pasword = driver.find_element_by_id("passwordLogin")
pasword.clear()
#mando pass
pasword.send_keys(contra)
#Press log in
driver.find_element_by_id("loginButton").click()

driver.implicitly_wait(10)

# seleccion de contrato
driver.find_element_by_id("111841").click()
# Ingreso a la pagina donde recupero los datos
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/section[1]/div/div/div/nav/ul/li[2]/a/span'))).click()

WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="scroll-orders-collapsible"]/li[1]/div[1]'))).click()

WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="dashboard-container"]/section/div/div/div/div/ul/li[2]/div/div/header/div/div/div[1]/div/div/div[2]'))).click()

WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div[5]/section/div/div/div/div/ul/li[2]/div/div/header/div/div/div[1]/div/div/div[3]/div/ul/li[2]'))).click()















