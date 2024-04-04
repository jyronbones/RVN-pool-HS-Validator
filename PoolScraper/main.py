from utils.proxy_manager import ProxyManager
from scrape.scraper import Scraper
from settings import SITE_URL


def main():
    proxy_manager = ProxyManager('resources/proxies.txt')
    proxy = proxy_manager.get_random_proxy()
    print(f"Using proxy: {proxy}")

    scraper = Scraper(SITE_URL)
    scraper.start(proxy)
    scraper.run()


if __name__ == "__main__":
    main()
