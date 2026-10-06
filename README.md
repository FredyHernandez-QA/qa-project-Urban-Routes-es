# Proyecto de Automatización de Pruebas: Urban Routes

## Descripción del Proyecto
Este proyecto consiste en la creación de un framework de automatización de pruebas de principio a fin (End-to-End) utilizando el patrón de diseño **Page Object Model (POM)**. El objetivo es validar de forma automatizada todo el flujo de solicitud de un taxi en la plataforma web **Urban Routes**, abarcando desde el ingreso de las direcciones hasta la confirmación de la asignación del conductor.

El flujo automatizado cubre los siguientes 9 criterios de aceptación del proyecto:
1. Configuración de la dirección de origen y destino.
2. Selección de la tarifa Comfort.
3. Validación y registro del número de teléfono mediante intercepción de código SMS.
4. Asociación de una tarjeta de crédito al método de pago (con pérdida de enfoque).
5. Envío de comentarios o mensajes especiales al conductor.
6. Solicitud de requisitos adicionales (manta y pañuelos).
7. Compra e incremento en el contador de helados.
8. Activación del modal de búsqueda de conductor.
9. Espera de la confirmación y asignación del vehículo en la interfaz.

## Tecnologías y Técnicas Utilizadas
* **Lenguaje de Programación:** Python 3
* **Herramienta de Automatización:** Selenium WebDriver
* **Framework de Pruebas:** Pytest
* **Patrón de Diseño:** Page Object Model (POM) para la separación limpia de localizadores (`locators.py`), acciones de página (`main.py`) y escenarios de prueba (`test_urban_routes.py`).
* **Esperas Explícitas (`WebDriverWait`):** Implementadas para asegurar la sincronización y robustez del código ante componentes asíncronos y animaciones web.

## Estructura del Repositorio
* `data.py`: Almacena todas las variables de prueba, credenciales simuladas y la URL dinámica del servidor.
* `locators.py`: Contiene los selectores e identificadores (ID, XPATH, CSS, Class Name) de los elementos web.
* `main.py`: Define los métodos y acciones de interacción correspondientes a la clase `UrbanRoutesPage`.
* `test_urban_routes.py`: Contiene la lógica de ejecución del flujo de pruebas y las aserciones (`assert`) de validación.

## Instrucciones de Configuración y Ejecución

### Prerrequisitos
Asegúrate de contar con Python instalado y las dependencias del archivo `requirements.txt` ejecutando en la terminal:
```bash
pip install -r requirements.txt
```

### Ejecución de las Pruebas
1. Inicia el servidor de pruebas en la plataforma de TripleTen para obtener la URL activa.
2. Actualiza la variable `urban_routes_url` dentro de tu archivo `data.py` en PyCharm con la dirección generada (asegúrate de incluir el sufijo `?lng=es`).
3. Abre la terminal integrada de PyCharm en la raíz del proyecto y ejecuta el siguiente comando:

```bash
pytest test_urban_routes.py -v
```