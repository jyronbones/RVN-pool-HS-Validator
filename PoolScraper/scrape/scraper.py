import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import settings
from configurations.driver_setup import WebDriverConfig
from settings import *


class Scraper:
    def __init__(self, site_url, db_manager):
        self.workers = None
        self.hash_rates = None
        self.earning_history = None
        self.wallet_stats = None
        self.site_url = site_url
        self.driver = None
        self.db_manager = db_manager

    def start(self, proxy):
        self.driver = WebDriverConfig.configure_driver(proxy)

    def get_element_text(self, xpath):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return element.text.strip()

    @staticmethod
    def clean_numeric(value):
        # Remove any non-numeric characters except for the decimal point
        cleaned_value = ''.join(c for c in value if c.isdigit() or c == '.')
        return float(cleaned_value) if cleaned_value else 0.0

    def scrape_wallet_stats(self):
        hash_rate = self.clean_numeric(self.get_element_text(WALLET_HASH_RATE))
        online_workers = int(self.clean_numeric(self.get_element_text(WALLET_ONLINE_WORKERS)))
        offline_workers = int(self.clean_numeric(self.get_element_text(WALLET_OFFLINE_WORKERS)))
        payout_coin = self.get_element_text(WALLET_PAYOUT_COIN)
        cleared_balance = self.clean_numeric(self.get_element_text(WALLET_CLEARED_BALANCE))
        self.wallet_stats = [hash_rate, online_workers, offline_workers, payout_coin, cleared_balance]

    def scrape_earning_history(self):
        self.earning_history = [
            self.get_element_text(EARNING_1_DAY),
            self.get_element_text(EARNING_7_DAYS),
            self.get_element_text(EARNING_14_DAYS),
            self.get_element_text(EARNING_30_DAYS)
        ]

    def scrape_hash_rates(self):
        self.hash_rates = [
            self.get_element_text(HASH_RATE_5_MIN),
            self.get_element_text(HASH_RATE_1_HOUR),
            self.get_element_text(HASH_RATE_6_HOURS),
            self.get_element_text(HASH_RATE_12_HOURS),
            self.get_element_text(HASH_RATE_24_HOURS)
        ]

    def scrape_workers(self):
        self.workers = []
        for i in range(1, 4):
            worker_stats = {
                'rig_name': self.get_element_text(getattr(settings, f'WORKER_{i}_RIG_NAME')),
                'hashrate': self.clean_numeric(self.get_element_text(getattr(settings, f'WORKER_{i}_HS'))),
                'difficulty': self.clean_numeric(self.get_element_text(getattr(settings, f'WORKER_{i}_DIFFICULTY'))),
                'spm': self.clean_numeric(self.get_element_text(getattr(settings, f'WORKER_{i}_SPM'))),
                'connect_time': self.get_element_text(getattr(settings, f'WORKER_{i}_CONNECT_TIME')),
                'last_seen': self.get_element_text(getattr(settings, f'WORKER_{i}_LAST_SEEN')),
                'last_share': self.get_element_text(getattr(settings, f'WORKER_{i}_LAST_SHARE')),
                'server': self.get_element_text(getattr(settings, f'WORKER_{i}_SERVER')),
                'type': self.get_element_text(getattr(settings, f'WORKER_{i}_TYPE')),
            }
            self.workers.append(worker_stats)

    def save_data(self):
        self.db_manager.connect()
        try:
            # Save the data using the DatabaseManager
            if self.wallet_stats:
                self.db_manager.insert_wallet_stats(tuple(self.wallet_stats))
            if self.earning_history:
                self.db_manager.insert_earning_history(tuple(self.earning_history))
            if self.hash_rates:
                self.db_manager.insert_hash_rates(tuple(self.hash_rates))
            for worker in self.workers:
                self.db_manager.insert_worker_data(worker)
        finally:
            self.db_manager.disconnect()

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
            self.save_data()
        finally:
            time.sleep(10)
            if self.driver:
                self.driver.quit()
