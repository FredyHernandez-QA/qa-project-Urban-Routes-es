import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# Corrección: Se importa retrieve_phone_code desde su archivo original independiente 'helpers'
from helpers import retrieve_phone_code
from main import UrbanRoutesPage


class TestUrbanRoutes:

    def setup_method(self):
        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(data.urban_routes_url)
        self.routes_page = UrbanRoutesPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    # Escenario 1: Ingresar Direcciones
    def test_set_route(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

    # Escenario 2: Seleccionar Tarifa Comfort
    def test_select_comfort_tariff(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.select_comfort_tariff()
        assert self.routes_page.is_comfort_tariff_selected() is True

    # Escenario 3: Validar e Interceptar Teléfono
    def test_fill_phone_number(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.select_comfort_tariff()

        self.routes_page.click_phone_field()
        self.routes_page.set_phone_number(data.phone_number)
        self.routes_page.click_next_phone_button()

        sms_code = retrieve_phone_code(self.driver)
        self.routes_page.set_sms_code(sms_code)
        self.routes_page.click_confirm_phone_button()

        assert self.routes_page.get_saved_phone_number() == data.phone_number

    # Escenario 4: Asociar Tarjeta de Crédito (con pérdida de foco)
    def test_add_credit_card(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.select_comfort_tariff()

        self.routes_page.click_payment_method()
        self.routes_page.click_add_card_button()
        self.routes_page.set_card_number(data.card_number)

        # Corrección: Se remueve interactuar con Keys y elementos directos desde el test. Lógica delegada al POM.
        self.routes_page.set_card_code_and_tab(data.card_code)

        self.routes_page.click_link_card_button()
        self.routes_page.click_close_payment_modal()
        assert self.routes_page.is_card_linked_successfully() is True

    # Escenario 5: Mensaje al Conductor
    def test_message_to_driver(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.select_comfort_tariff()

        self.routes_page.set_driver_message(data.message_for_driver)
        # Corrección: Se remueve el uso directo de get_property en las aserciones del test.
        assert self.routes_page.get_driver_message() == data.message_for_driver

    # Escenario 6: Manta y Pañuelos
    def test_blanket_and_tissues_requirement(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.select_comfort_tariff()

        self.routes_page.toggle_blanket_and_tissues()
        assert self.routes_page.is_blanket_toggle_checked() is True

    # Escenario 7: Pedir 2 Helados
    def test_add_two_ice_creams(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.select_comfort_tariff()

        self.routes_page.click_add_ice_cream_button()
        self.routes_page.click_add_ice_cream_button()
        assert self.routes_page.get_ice_cream_counter_value() == "2"

    # Escenario 8: Solicitar Taxi (Aparición del Modal)
    def test_request_taxi_final(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.select_comfort_tariff()

        # Corrección: Agregadas las precondiciones completas indispensables (Teléfono + Tarjeta) para que el modal final aparezca.
        self.routes_page.click_phone_field()
        self.routes_page.set_phone_number(data.phone_number)
        self.routes_page.click_next_phone_button()
        sms_code = retrieve_phone_code(self.driver)
        self.routes_page.set_sms_code(sms_code)
        self.routes_page.click_confirm_phone_button()

        self.routes_page.click_payment_method()
        self.routes_page.click_add_card_button()
        self.routes_page.set_card_number(data.card_number)
        self.routes_page.set_card_code_and_tab(data.card_code)
        self.routes_page.click_link_card_button()
        self.routes_page.click_close_payment_modal()

        self.routes_page.set_driver_message(data.message_for_driver)
        self.routes_page.click_final_order_button()
        assert self.routes_page.is_search_modal_visible() is True

    # Escenario 9: Esperar Información Asignada del Conductor
    def test_driver_assignment_info(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.select_comfort_tariff()

        # Corrección: Agregadas las precondiciones de teléfono y tarjeta para que el flujo sea exitoso y asigne un chofer
        self.routes_page.click_phone_field()
        self.routes_page.set_phone_number(data.phone_number)
        self.routes_page.click_next_phone_button()
        sms_code = retrieve_phone_code(self.driver)
        self.routes_page.set_sms_code(sms_code)
        self.routes_page.click_confirm_phone_button()

        self.routes_page.click_payment_method()
        self.routes_page.click_add_card_button()
        self.routes_page.set_card_number(data.card_number)
        self.routes_page.set_card_code_and_tab(data.card_code)
        self.routes_page.click_link_card_button()
        self.routes_page.click_close_payment_modal()

        self.routes_page.set_driver_message(data.message_for_driver)
        self.routes_page.click_final_order_button()

        # Corrección: Se evalúa el texto del componente dinámico real devuelto en vez de conformarse con un True genérico
        driver_text = self.routes_page.wait_for_driver_assignment()
        assert driver_text not in ["", "Buscar automóvil"]