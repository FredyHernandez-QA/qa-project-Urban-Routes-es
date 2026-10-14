import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import UrbanRoutesLocators

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    # Espera explícita genérica para legibilidad
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    # --- ESCENARIO 1: Configurar Direcciones ---
    def set_from(self, address_from):
        field = self.wait_for_element(UrbanRoutesLocators.FROM_FIELD)
        field.send_keys(address_from)

    def set_to(self, address_to):
        field = self.wait_for_element(UrbanRoutesLocators.TO_FIELD)
        field.send_keys(address_to)

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def get_from(self):
        return self.wait_for_element(UrbanRoutesLocators.FROM_FIELD).get_property('value')

    def get_to(self):
        return self.wait_for_element(UrbanRoutesLocators.TO_FIELD).get_property('value')

    # --- ESCENARIO 2: Tarifa Comfort ---
    def click_request_taxi_button(self):
        # Corrección: Eliminados los imports duplicados de adentro y se captura TimeoutException específicamente
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(UrbanRoutesLocators.REQUEST_TAXI_BUTTON)
            ).click()
        except TimeoutException:
            raise AssertionError("El botón para pedir taxi inicial no estuvo disponible o clickeable.")

    def select_comfort_tariff(self):
        self.wait_for_element(UrbanRoutesLocators.COMFORT_TARIFF_CARD).click()

    def is_comfort_tariff_selected(self):
        try:
            return self.wait_for_element(UrbanRoutesLocators.COMFORT_TARIFF_ACTIVE, timeout=3).is_displayed()
        except TimeoutException:
            return False

    # --- ESCENARIO 3: Teléfono ---
    def click_phone_field(self):
        self.wait_for_element(UrbanRoutesLocators.PHONE_FIELD).click()

    def set_phone_number(self, phone):
        self.wait_for_element(UrbanRoutesLocators.PHONE_INPUT).send_keys(phone)

    def click_next_phone_button(self):
        self.wait_for_element(UrbanRoutesLocators.NEXT_PHONE_BUTTON).click()

    def set_sms_code(self, code):
        self.wait_for_element(UrbanRoutesLocators.SMS_CODE_INPUT).send_keys(code)

    def click_confirm_phone_button(self):
        self.wait_for_element(UrbanRoutesLocators.CONFIRM_PHONE_BUTTON).click()

    def get_saved_phone_number(self):
        return self.wait_for_element(UrbanRoutesLocators.SAVED_PHONE_NUMBER).text

    # --- ESCENARIO 4: Tarjeta de Crédito ---
    def click_payment_method(self):
        self.wait_for_element(UrbanRoutesLocators.PAYMENT_METHOD_BUTTON).click()

    def click_add_card_button(self):
        self.wait_for_element(UrbanRoutesLocators.ADD_CARD_BUTTON).click()

    def set_card_number(self, number):
        self.wait_for_element(UrbanRoutesLocators.CARD_NUMBER_INPUT).send_keys(number)

    # Corrección: Se encapsula el envío de Keys.TAB dentro del Page Object para no exponer lógica de Selenium en el test
    def set_card_code_and_tab(self, code):
        field = self.wait_for_element(UrbanRoutesLocators.CARD_CODE_INPUT)
        field.send_keys(code)
        field.send_keys(Keys.TAB)

    def click_link_card_button(self):
        self.wait_for_element(UrbanRoutesLocators.LINK_CARD_BUTTON).click()

    def click_close_payment_modal(self):
        self.wait_for_element(UrbanRoutesLocators.CLOSE_PAYMENT_MODAL).click()

    def is_card_linked_successfully(self):
        return self.driver.find_element(*UrbanRoutesLocators.LINKED_CARD_CHECKBOX).is_selected()

    # --- ESCENARIO 5: Mensaje al conductor ---
    def set_driver_message(self, message):
        self.wait_for_element(UrbanRoutesLocators.DRIVER_MESSAGE_INPUT).send_keys(message)

    # Corrección: Extrae el valor directamente en el método para limpiar la aserción en el archivo de pruebas
    def get_driver_message(self):
        return self.wait_for_element(UrbanRoutesLocators.DRIVER_MESSAGE_INPUT).get_property('value')

    # --- ESCENARIO 6: Manta y Pañuelos ---
    def toggle_blanket_and_tissues(self):
        element = self.driver.find_element(*UrbanRoutesLocators.BLANKET_SWITCH)
        self.driver.execute_script("arguments[0].click();", element)

    def is_blanket_toggle_checked(self):
        return self.driver.find_element(*UrbanRoutesLocators.BLANKET_SWITCH).is_selected()

    # --- ESCENARIO 7: Helados ---
    def click_add_ice_cream_button(self):
        self.wait_for_element(UrbanRoutesLocators.ICE_CREAM_PLUS_BUTTON).click()

    def get_ice_cream_counter_value(self):
        return self.wait_for_element(UrbanRoutesLocators.ICE_CREAM_COUNTER).text

    # --- ESCENARIO 8: Pedir Taxi ---
    def click_final_order_button(self):
        self.wait_for_element(UrbanRoutesLocators.FINAL_ORDER_BUTTON).click()

    def is_search_modal_visible(self):
        return self.wait_for_element(UrbanRoutesLocators.SEARCH_MODAL).is_displayed()

    # --- ESCENARIO 9: Esperar Asignación de Conductor ---
    def wait_for_driver_assignment(self):
        # Corrección: Se utiliza la condición lambda para ignorar de forma explícita los estados intermedios como 'Buscar automóvil'
        WebDriverWait(self.driver, 60).until(
            lambda d: d.find_element(*UrbanRoutesLocators.DRIVER_INFO_HEADER).text not in ["", "Buscar automóvil"]
        )
        return self.driver.find_element(*UrbanRoutesLocators.DRIVER_INFO_HEADER).text