from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import multiprocessing

# URL del formulario de Google
url = "https://forms.gle/tyR1NwSvWNiFT2Ar6"


# Configura los pesos para cada pregunta
def responder_formulario():
    # Configuración del driver de Selenium
    driver = webdriver.Chrome()
    driver.get(url)

    try:
        # Número de veces que cada instancia enviará el formulario
        num_repeticiones = 10

        for i in range(num_repeticiones):
            wait = WebDriverWait(driver, 10)
            # Primera página: clic en "Sí" y "Siguiente"
            opcion_si = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "/html/body/div/div[2]/form/div[2]/div/div[2]/div/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div",
                    )
                )
            )
            opcion_si.click()

            boton_siguiente = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "/html/body/div/div[2]/form/div[2]/div/div[3]/div/div[1]/div/span",
                    )
                )
            )
            boton_siguiente.click()

            time.sleep(1)  # Espera breve para cargar la segunda página

            # Segunda página: Selección aleatoria con inclinación para cada pregunta

            # Pregunta "Edad"
            opciones_edad = [
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div",
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]",
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]",
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[1]/div/div[3]",
            ]
            opcion_elegida = random.choices(
                opciones_edad, weights=[25, 25, 25, 25], k=1
            )[0]
            wait.until(EC.element_to_be_clickable((By.XPATH, opcion_elegida))).click()

            # Pregunta "Género"
            opciones_genero = ["//*[@id='i23']", "//*[@id='i26']"]
            opcion_elegida = random.choices(opciones_genero, weights=[50, 50], k=1)[0]
            wait.until(EC.element_to_be_clickable((By.XPATH, opcion_elegida))).click()

            # Pregunta "Zona de residencia"
            opciones_residencia = [
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]/label",
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[2]/label",
            ]
            opcion_elegida = random.choices(opciones_residencia, weights=[20, 80], k=1)[
                0
            ]
            wait.until(EC.element_to_be_clickable((By.XPATH, opcion_elegida))).click()

            # Pregunta "¿Conoce algún sitio histórico o lugar patrimonial en Coronel?"
            opciones_conocimiento = [
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[1]/label",
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[2]/label",
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[3]/label",
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[4]/label",
            ]
            opcion_elegida = random.choices(
                opciones_conocimiento, weights=[70, 10, 10, 10], k=1
            )[0]
            wait.until(EC.element_to_be_clickable((By.XPATH, opcion_elegida))).click()

            # Pregunta "¿Conoce alguna de las tradiciones culturales de Coronel, como festivales o celebraciones locales?"
            opciones_tradiciones = [
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[1]/label",
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[2]/label",
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[3]/label",
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[4]/label",
            ]
            opcion_elegida = random.choices(
                opciones_tradiciones, weights=[30, 30, 30, 10], k=1
            )[0]
            wait.until(EC.element_to_be_clickable((By.XPATH, opcion_elegida))).click()

            # Pregunta "En una escala del 1 al 5..."
            opciones_importancia = [
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div",  # 1
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div",  # 2
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div",  # 3
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div",  # 4
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div",  # 5
            ]
            opcion_elegida = random.choices(
                opciones_importancia, weights=[5, 10, 10, 15, 60], k=1
            )[0]
            wait.until(EC.element_to_be_clickable((By.XPATH, opcion_elegida))).click()

            # Pregunta "¿Qué tan de acuerdo está con la afirmación..."
            opciones_acuerdo = [
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[1]/label",
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[2]/label",
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[3]/label",
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[4]/label",
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[5]/label",
            ]
            opcion_elegida = random.choices(
                opciones_acuerdo, weights=[5, 10, 10, 15, 60], k=1
            )[0]
            wait.until(EC.element_to_be_clickable((By.XPATH, opcion_elegida))).click()

            # Pregunta "¿Ha notado alguna campaña reciente..."
            opciones_campana = [
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[1]/label",
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[2]/label",
            ]
            opcion_elegida = random.choices(opciones_campana, weights=[30, 70], k=1)[0]
            wait.until(EC.element_to_be_clickable((By.XPATH, opcion_elegida))).click()

            # Pregunta "¿Qué tan efectiva cree que ha sido la Municipalidad..."
            opciones_efectividad = [
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[1]/label",
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[2]/label",
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[3]/label",
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[4]/label",
            ]
            opcion_elegida = random.choices(
                opciones_efectividad, weights=[90, 3, 3, 4], k=1
            )[0]
            wait.until(EC.element_to_be_clickable((By.XPATH, opcion_elegida))).click()

            # Botón "Enviar"
            boton_enviar = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//*[@id='mG61Hd']/div[2]/div/div[3]/div/div[1]/div[2]/span",
                    )
                )
            )
            boton_enviar.click()
            print(f"Formulario enviado con éxito. Repetición {i + 1}.")

            # Espera breve para cargar la página de confirmación
            time.sleep(1)

            # Clic en "Enviar otra respuesta"
            boton_otra_respuesta = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
                )
            )
            boton_otra_respuesta.click()

            # Espera breve antes de iniciar el siguiente ciclo
            time.sleep(1)

    except Exception as e:
        print(f"Error durante la automatización: {e}")
    finally:
        # Cierra el navegador
        driver.quit()


# Ejecuta múltiples instancias en paralelo
if __name__ == "__main__":
    # Número de procesos paralelos (ajusta según tu sistema)
    num_procesos = 4
    procesos = []

    for _ in range(num_procesos):
        proceso = multiprocessing.Process(target=responder_formulario)
        proceso.start()
        procesos.append(proceso)

    for proceso in procesos:
        proceso.join()
