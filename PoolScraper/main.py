from configurations.driver_setup import configure_driver
from utils.proxy_manager import read_proxies
import random
import time
from settings import SITE_URL


def main():
    proxies = read_proxies('resources/proxies.txt')
    proxy = random.choice(proxies) if proxies else None
    print(f"Using proxy: {proxy}")

    # Configure driver with proxy
    driver = configure_driver(proxy)

    # Navigate to the page
    url = SITE_URL
    print(f"Accessing {url}")
    driver.get(url)

    # Add a delay
    time.sleep(10)

    driver.quit()


if __name__ == "__main__":
    main()
