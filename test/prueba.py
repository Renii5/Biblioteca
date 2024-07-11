from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://localhost:3005")

time.sleep(3)

#--------------------------------------------------------------------------

# DAR DE ALTA UN LIBRO VALIDO
# Para que sea invalido correrlo por 2 vez 

driver.find_element(By.LINK_TEXT, "Alta").click()
time.sleep(2)

driver.find_element(By.ID, "isbn").send_keys("1235343")
driver.find_element(By.ID, "titulo").send_keys("Cenicienta")
driver.find_element(By.ID, "autor_nombre").send_keys("Juan")
driver.find_element(By.ID, "autor_apellido").send_keys("Gonzalez")
driver.find_element(By.ID, "anio").send_keys("pppp")
driver.find_element(By.ID, "genero").send_keys("Ficcion")
driver.find_element(By.ID, "paginas").send_keys("200")
driver.find_element(By.ID, "editorial").send_keys("Editorial")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)  

error_message = None
try:
    error_message = driver.find_element(By.XPATH, "XPATH_DEL_MENSAJE_DE_ERROR").text
except:
    pass

if error_message and "ISBN ya existe" in error_message:
    driver.execute_script("alert('ISBN no valido');")

driver.find_element(By.LINK_TEXT, "Home").click()
time.sleep(5)

driver.quit()


#--------------------------------------------------------------------------

# DAR DE BAJA UN LIBRO
# driver.find_element(By.LINK_TEXT, "Baja").click()
# time.sleep(2)

# driver.find_element(By.ID, "isbn").send_keys("1920123814")
# driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()  # Asegúrate de que apunte al botón correcto

# time.sleep(2) 
# driver.find_element(By.LINK_TEXT, "Home").click()

# time.sleep(5)


#--------------------------------------------------------------------------

#DAR DE BAJA UN LIBRO QUE NO EXISTE
# driver.find_element(By.LINK_TEXT, "Baja").click()
# time.sleep(2)

# driver.find_element(By.ID, "isbn").send_keys("9999999999")

# driver.find_element(By.LINK_TEXT, "Home").click()

#--------------------------------------------------------------------------

# MODIFICAR UN LIBRO
# driver.find_element(By.LINK_TEXT, "Modificar").click()
# time.sleep(2)

# driver.find_element(By.ID, "titulo").clear()
# driver.find_element(By.ID, "titulo").send_keys("El libro de la selva")
# driver.find_element(By.ID, "autor_nombre").clear()
# driver.find_element(By.ID, "autor_nombre").send_keys("Nicolas")
# driver.find_element(By.ID, "autor_apellido").clear()
# driver.find_element(By.ID, "autor_apellido").send_keys("Lopez")
# driver.find_element(By.ID, "anio").clear()
# driver.find_element(By.ID, "anio").send_keys("2023")
# driver.find_element(By.ID, "genero").clear()
# driver.find_element(By.ID, "genero").send_keys("Fantasia")
# driver.find_element(By.ID, "paginas").clear()
# driver.find_element(By.ID, "paginas").send_keys("350")
# driver.find_element(By.ID, "editorial").clear()
# driver.find_element(By.ID, "editorial").send_keys("Bel")

# driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()  # Asegúrate de que apunte al botón correcto
# time.sleep(2)

# driver.find_element(By.LINK_TEXT, "Home").click()
# time.sleep(5)


#--------------------------------------------------------------------------

# MODIFICAR EL SEGUNDO LIBRO
# driver.find_elements(By.LINK_TEXT, "Modificar")[1].click()  
# time.sleep(2)

# driver.find_element(By.ID, "titulo").clear()
# driver.find_element(By.ID, "titulo").send_keys("Libro Modificado")
# driver.find_element(By.ID, "autor_nombre").clear()
# driver.find_element(By.ID, "autor_nombre").send_keys("Autor2")
# driver.find_element(By.ID, "autor_apellido").clear()
# driver.find_element(By.ID, "autor_apellido").send_keys("Apellido2")
# driver.find_element(By.ID, "anio").clear()
# driver.find_element(By.ID, "anio").send_keys("2023")
# driver.find_element(By.ID, "genero").clear()
# driver.find_element(By.ID, "genero").send_keys("Ficcion")
# driver.find_element(By.ID, "paginas").clear()
# driver.find_element(By.ID, "paginas").send_keys("200")
# driver.find_element(By.ID, "editorial").clear()
# driver.find_element(By.ID, "editorial").send_keys("Editorial")

# driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()  # Asegúrate de que apunte al botón correcto
# time.sleep(2)

# driver.find_element(By.LINK_TEXT, "Home").click()
# time.sleep(5)

#--------------------------------------------------------------------------


driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

input("Presiona Enter para cerrar el navegador...")

driver.quit()  # Cerrar el navegador
