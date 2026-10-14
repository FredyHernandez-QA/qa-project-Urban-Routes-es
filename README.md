# Proyecto Urban Routes - Proyecto de Automatización de Pruebas: Urban Routes

Este proyecto contiene la suite de pruebas automatizadas para la aplicación Urban Routes utilizando Python y Selenium WebDriver bajo el patrón de diseño Page Object Model (POM).

## 🛠️ Instalación

```bash
git clone <url_del_repositorio>
cd qa-project-Urban-Routes-es
pip install selenium pytest
```

## 🚀 Ejecución de las Pruebas

Para correr la suite completa de pruebas, ejecuta:
```bash
pytest test_urban_routes.py
```

## 📂 Estructura del Proyecto

* `data.py`: Contiene los datos estáticos de prueba (direcciones, teléfono, tarjeta, etc.).
* `locators.py`: Centraliza todos los selectores de elementos web (clase UrbanRoutesLocators).
* `main.py`: Contiene los Page Objects con los métodos de interacción de la interfaz.
* `test_urban_routes.py`: Contiene los 9 escenarios de prueba independientes y sus aserciones.
* `helpers.py`: Función utilitaria para recuperar el código SMS de confirmación.

## 📋 Escenarios Cubiertos (9/9)

1. Configurar la dirección de origen y destino.
2. Seleccionar la tarifa Comfort.
3. Rellenar el número de teléfono.
4. Agregar una tarjeta de crédito/débito.
5. Escribir un mensaje para el conductor.
6. Pedir una manta y pañuelos.
7. Pedir 2 helados.
8. Esperar a que aparezca el modal con la información del conductor.
9. Validar el flujo final del pedido de taxi.