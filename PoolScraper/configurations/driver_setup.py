from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class WebDriverConfig:
    @staticmethod
    def configure_driver(proxy=None):
        print('Configuring driver...')
        seleniumwire_options = {
            'proxy': {
                'http': f'http://{proxy}',
                'https': f'https://{proxy}',
                'no_proxy': 'localhost,127.0.0.1'
            }
        } if proxy else {}

        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = True
        chrome_options.add_argument('start-maximized')
        chrome_options.add_argument("window-size=1900,1080")
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/87.0.4280.141 Safari/537.36"
        )

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                  seleniumwire_options=seleniumwire_options,
                                  options=chrome_options)
        return driver
