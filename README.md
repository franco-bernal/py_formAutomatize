
# Instrucciones para configurar y activar un entorno virtual en Python

## 1. Crear un entorno virtual
1. Abre la terminal o línea de comandos en la carpeta raíz de tu proyecto.
2. Ejecuta el siguiente comando para crear un entorno virtual llamado `env`:

   ```bash
   python -m venv env
   ```

   Esto creará una carpeta `env` con todos los archivos necesarios para el entorno virtual.

---

## 2. Activar el entorno virtual
Dependiendo de tu sistema operativo, el comando para activar el entorno varía:

- **En Windows**:
  ```bash
  env\Scripts\activate
  ```

- **En macOS o Linux**:
  ```bash
  source env/bin/activate
  ```

---

## 3. Instalar selenium

- **comando**:
  ```bash
  pip install selenium
  ```

---

## 4. ajustar Xpath

- En esta sección ya sólo faltaría configurar los XPath de las respuestas y sus pesos en el código. 
- el "Copy full XPath" es más confiable.
- los pesos ayudarán para ajustar si en alguna pregunta se desea que se responda más una alternativa que otra.
  
---

## 4. En caso de falla revisar XPath

- la ultima vez me sucedió que dejaron de funcionar los xpath porque se habían actualizado de una semana para otra. 