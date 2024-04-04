from configurations.driver_setup import WebDriverConfig
import time


class Scraper:
    def __init__(self, site_url):
        self.site_url = site_url
        self.driver = None

    def start(self, proxy):
        self.driver = WebDriverConfig.configure_driver(proxy)

    def scrape(self):
        print(f"Accessing {self.site_url}")
        self.driver.get(self.site_url)
        # ... additional scraping logic ...

    def run(self):
        try:
            self.scrape()
            # Add any post-scraping actions (e.g., saving data)
        finally:
            time.sleep(10)  # Delay for observing the browser
            self.driver.quit()
