# Прописываем в терминале:
# python -m pip install --upgrade pip (Обновление менеджера пакетов pip)
# pip install selenium (Устанавливаем библиотеку selenium)
# pip install webdriver-manager (Устанавливаем webdriver-manager)
import time

# импортируем необходимые библиотеки и элементы
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# создаем и настраиваем экземпляр driver класса webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# создаем переменную содержащую базовую ссылку и открываем её с помощью созданного ранее driver
base_url = 'http://demoqa.com/radio-button'
driver.get(base_url)
driver.maximize_window()

# создаем переменную для радио-кнопки и нажимаем
radio_button = driver.find_element(By.XPATH, "(//label[@class='custom-control-label'])[2]")
radio_button.click()
print('Произведен клик по кнопке')

# проверяем активацию радио-кнопки
value_radio_button = driver.find_element(By.XPATH, "//p[@class='mt-3']").text
print(f'Сообщение на сайте гласит: {value_radio_button}')
assert value_radio_button == 'You have selected Impressive', 'Radio Button not selected'
print('Кнопка "Impressive" успешно выбрана')