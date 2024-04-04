import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import settings
from configurations.driver_setup import WebDriverConfig
from settings import *
import threading
import keyboard


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

    def get_element_text_with_wait(self, xpath, timeout=10, poll_frequency=0.5):
        """
        Wait for the element text to change from its initial value within a timeout period.
        Polls the element's text at specified intervals.
        """
        end_time = time.time() + timeout
        while True:
            try:
                element_text = self.get_element_text(xpath)
                if element_text != "0":
                    return element_text
            except Exception as e:
                print(f"Error while waiting for element text to change: {e}")
            time.sleep(poll_frequency)  # Wait before checking again
            if time.time() > end_time:
                break
        return "-1"

    def scrape_wallet_stats(self):
        hash_rate = self.clean_numeric(self.get_element_text(WALLET_HASH_RATE))
        online_workers_text = self.get_element_text_with_wait(WALLET_ONLINE_WORKERS, timeout=5)
        online_workers = int(self.clean_numeric(online_workers_text))
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
        self.driver.get(self.site_url)
        time.sleep(2)
        self.scrape_wallet_stats()
        self.scrape_earning_history()
        self.scrape_hash_rates()
        self.scrape_workers()

    def run(self):
        stop_flag = threading.Event()

        def wait_for_exit_command():
            print("Press CTRL+SHIFT+Q to stop the scraper at any time...")
            keyboard.add_hotkey('ctrl+shift+q', lambda: stop_flag.set())
            keyboard.wait('ctrl+shift+q')
            if self.driver:
                self.driver.quit()

        # Start the thread that will wait for the input
        exit_thread = threading.Thread(target=wait_for_exit_command)
        exit_thread.start()

        refresh_counter = 0
        try:
            while not stop_flag.is_set():  # Run until the flag is set
                self.scrape()
                self.save_data()
                time.sleep(15)
                refresh_counter += 1
                time.sleep(1)
                if refresh_counter >= 30:
                    self.driver.refresh()
                    refresh_counter = 0

        finally:
            if not stop_flag.is_set():
                # If the flag is not set, it means the loop was interrupted unexpectedly
                stop_flag.set()
            exit_thread.join()  # Wait for the exit command thread to finish
            if self.driver:
                self.driver.quit()  # Close the browser window
            print("Scraper has been stopped.")
