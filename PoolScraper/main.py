from utils.proxy_manager import ProxyManager
from utils.database_manager import DatabaseManager
from scrape.scraper import Scraper
from settings import SITE_URL, DB_CONNECTION_STRING


def main():
    proxy_manager = ProxyManager('resources/proxies.txt')
    proxy = proxy_manager.get_random_proxy()
    print(f"Using proxy: {proxy}")

    # Initialize the DatabaseManager with the connection string from settings.py
    db_manager = DatabaseManager(DB_CONNECTION_STRING)

    # Create the Scraper instance with the database manager
    scraper = Scraper(SITE_URL, db_manager)
    scraper.start(proxy)
    scraper.run()  # Also inserts data into DB


if __name__ == "__main__":
    main()
