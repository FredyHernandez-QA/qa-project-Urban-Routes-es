# Proyecto 9 - Proyecto de Automatización de Pruebas: Urban Routes

Este proyecto consiste en el desarrollo y reestructuración completa de un framework de pruebas automatizadas para la aplicación **Urban Routes**, aplicando de forma estricta el patrón de diseño **Page Object Model (POM)** en Python con Selenium WebDriver y PyTest.

La arquitectura del proyecto ha sido corregida a nivel profundo para garantizar la modularidad de los componentes y la total independencia de los casos de prueba, cumpliendo al 100% con las observaciones técnicas recibidas en la revisión de código.

---

## 📁 Estructura General del Proyecto

El código se encuentra distribuido de forma modular en 4 archivos principales:

*   **`data.py`**: Centraliza todas las variables globales y los datos de prueba del entorno (URLs, direcciones, número telefónico, datos de tarjetas de crédito y mensajes para el conductor).
*   **`locators.py`**: Contiene exclusivamente la clase `UrbanRoutesLocators`, donde se almacenan las tuplas de localización. Cumple con el requisito de utilizar una variedad diversa de estrategias de búsqueda (`By.ID`, `By.CLASS_NAME`, `By.XPATH` y `By.CSS_SELECTOR`).
*   **`main.py`**: Contiene la clase `UrbanRoutesPage`, encargada únicamente de los métodos de interacción con los elementos de la página web (acciones de clic, ingreso de texto, obtención de propiedades y esperas explícitas). También aloja la función auxiliar de red para interceptar el código SMS.
*   **`test_urban_routes.py`**: Contiene la clase de pruebas `TestUrbanRoutes`. Implementa los métodos de ciclo de vida (`setup_method` y `teardown_method`) para aislar completamente cada escenario.

---

## 🛠️ Correcciones Implementadas en esta Versión

1.  **Independencia de Pruebas (Ciclo de Vida Limpio)**: Se eliminó el uso de métodos de clase (`setup_class` / `teardown_class`). Ahora se utilizan `setup_method(self)` y `teardown_method(self)`. Esto garantiza que **cada prueba abra una ventana de Chrome desde cero**, eliminando dependencias de estado o sesiones previas.
2.  **Cobertura Total (Los 9 Escenarios)**: Se expandió el archivo de pruebas para cubrir los 9 escenarios requeridos por el proyecto, asegurando que cada método `test_...` ejecute de manera autónoma sus propias precondiciones de flujo.
3.  **Solución al `AttributeError`**: Se implementó el método contenedor `set_route(self, address_from, address_to)` dentro de `main.py`, resolviendo directamente el error de atributo que causaba la detención de las ejecuciones.
4.  **Formato de Datos Corregido**: Se limpió la variable `phone_number` en `data.py` eliminando los espacios internos en blanco para que la API de Urban Routes procese de manera óptima el envío del SMS de verificación.
5.  **Pérdida de Foco en Tarjeta**: Se integró el uso de `Keys.TAB` en la confirmación del código de seguridad de la tarjeta de crédito para simular de forma realista la pérdida de foco exigida.
6.  **Aserciones Robustas**: Se migró la validación del mensaje al conductor utilizando la propiedad interna del elemento mediante `.get_property('value')`.

---

## 🚀 Ejecución de las Pruebas

Para ejecutar el set completo de pruebas modulares de manera local, abre la terminal del proyecto en tu entorno virtual y ejecuta el siguiente comando:

```bash
pytest test_urban_routes.py
```

*Nota sobre el entorno: En caso de experimentar latencia o intermitencias con el mensaje "Introduzca dirección" debido a fallas de comunicación en las APIs de mapas internas del contenedor del simulador, se recomienda restablecer el contenedor de la plataforma para limpiar la base de datos del servidor local.*