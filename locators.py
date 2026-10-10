from selenium.webdriver.common.by import By


class UrbanRoutesLocators:
    # 1. Direcciones (Uso de By.ID)
    FROM_FIELD = (By.ID, 'from')
    TO_FIELD = (By.ID, 'to')

    # 2. Tarifas (Uso de By.XPATH y By.CLASS_NAME)
    REQUEST_TAXI_BUTTON = (By.XPATH, '//button[contains(@class, "smart-button")]')
    COMFORT_TARIFF_CARD = (By.XPATH, '//div[contains(@class, "txi-card")]//div[text()="Comfort"]')
    COMFORT_TARIFF_ACTIVE = (By.XPATH, '//div[@class="txi-card active"]//div[text()="Comfort"]')

    # 3. Teléfono (Uso de By.CLASS_NAME y By.CSS_SELECTOR)
    PHONE_FIELD = (By.CLASS_NAME, 'np-text')
    PHONE_INPUT = (By.ID, 'phone')
    NEXT_PHONE_BUTTON = (By.XPATH, '//button[text()="Siguiente"]')
    SMS_CODE_INPUT = (By.ID, 'code')
    CONFIRM_PHONE_BUTTON = (By.XPATH, '//button[text()="Confirmar"]')
    SAVED_PHONE_NUMBER = (By.CLASS_NAME, 'np-value')

    # 4. Tarjeta de Crédito
    PAYMENT_METHOD_BUTTON = (By.CLASS_NAME, 'pp-text')
    ADD_CARD_BUTTON = (By.XPATH, '//div[text()="Agregar tarjeta"]')
    CARD_NUMBER_INPUT = (By.ID, 'number')
    CARD_CODE_INPUT = (By.XPATH, '//div[@class="card-code-input"]//input[@id="code"]')
    LINK_CARD_BUTTON = (By.XPATH, '//button[text()="Enlazar"]')
    CLOSE_PAYMENT_MODAL = (By.CSS_SELECTOR, '.payment-picker .close-button')
    LINKED_CARD_CHECKBOX = (By.XPATH, '//input[@class="checkbox" and @type="checkbox"]')

    # 5. Requisitos adicionales (Uso de By.CSS_SELECTOR y By.XPATH)
    DRIVER_MESSAGE_INPUT = (By.ID, 'comment')
    BLANKET_SWITCH = (By.CSS_SELECTOR, '.r-type-switch .switch-input')
    ICE_CREAM_PLUS_BUTTON = (By.XPATH, '//div[text()="Helado"]/..//div[@class="counter-plus"]')
    ICE_CREAM_COUNTER = (By.XPATH, '//div[text()="Helado"]/..//div[@class="counter-value"]')

    # 6. Flujo de Pedido Final
    FINAL_ORDER_BUTTON = (By.CLASS_NAME, 'smart-button')
    SEARCH_MODAL = (By.CLASS_NAME, 'order-body')
    DRIVER_INFO_HEADER = (By.XPATH, '//div[contains(@class, "order-header-title")]')