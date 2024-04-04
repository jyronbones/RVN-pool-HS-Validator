import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from configurations.driver_setup import WebDriverConfig
from settings import *


class Scraper:
    def __init__(self, site_url):
        self.site_url = site_url
        self.driver = None
        # Initialize all data lists
        self.wallet_stats = []
        self.earning_history = []
        self.hash_rates = []
        self.workers = []

    def start(self, proxy):
        self.driver = WebDriverConfig.configure_driver(proxy)

    def get_element_text(self, xpath):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return element.text

    def scrape_wallet_stats(self):
        self.wallet_stats.append(self.get_element_text(WALLET_HASH_RATE))
        self.wallet_stats.append(self.get_element_text(WALLET_ONLINE_WORKERS))
        self.wallet_stats.append(self.get_element_text(WALLET_OFFLINE_WORKERS))
        self.wallet_stats.append(self.get_element_text(WALLET_PAYOUT_COIN))
        self.wallet_stats.append(self.get_element_text(WALLET_CLEARED_BALANCE))

    def scrape_earning_history(self):
        self.earning_history.append(self.get_element_text(EARNING_1_DAY))
        self.earning_history.append(self.get_element_text(EARNING_7_DAYS))
        self.earning_history.append(self.get_element_text(EARNING_14_DAYS))
        self.earning_history.append(self.get_element_text(EARNING_30_DAYS))

    def scrape_hash_rates(self):
        self.hash_rates.append(self.get_element_text(HASH_RATE_5_MIN))
        self.hash_rates.append(self.get_element_text(HASH_RATE_1_HOUR))
        self.hash_rates.append(self.get_element_text(HASH_RATE_6_HOURS))
        self.hash_rates.append(self.get_element_text(HASH_RATE_12_HOURS))
        self.hash_rates.append(self.get_element_text(HASH_RATE_24_HOURS))

    def scrape_workers(self):
        # Assuming that you have the same number of attributes for each worker
        for i in range(1, 4):  # Adjust the range if there are more workers
            worker_stats = [
                self.get_element_text(eval(f'WORKER_{i}_RIG_NAME')),
                self.get_element_text(eval(f'WORKER_{i}_HS')),
                self.get_element_text(eval(f'WORKER_{i}_DIFFICULTY')),
                self.get_element_text(eval(f'WORKER_{i}_SPM')),
                self.get_element_text(eval(f'WORKER_{i}_CONNECT_TIME')),
                self.get_element_text(eval(f'WORKER_{i}_LAST_SEEN')),
                self.get_element_text(eval(f'WORKER_{i}_LAST_SHARE')),
                self.get_element_text(eval(f'WORKER_{i}_SERVER')),
                self.get_element_text(eval(f'WORKER_{i}_TYPE')),
            ]
            self.workers.append(worker_stats)

    def scrape(self):
        print(f"Accessing {self.site_url}")
        self.driver.get(self.site_url)
        self.scrape_wallet_stats()
        self.scrape_earning_history()
        self.scrape_hash_rates()
        self.scrape_workers()

    def run(self):
        try:
            self.scrape()
            # Here you would have the option to call another method to insert data into the database
        finally:
            time.sleep(10)  # Delay for observing the browser
            self.driver.quit()
