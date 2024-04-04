from dotenv import load_dotenv
import os

load_dotenv()

DB_CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING")

SITE_URL = "https://www.ravenminer.com/ravencoin/wallet/REuaQ4hVkipRsu6tX27iENPrHxGpvfkFh9"

# Scraper values Wallet Stats
WALLET_HASH_RATE = "/html/body/main/div[4]/div[1]/div[1]/div[1]/div/div[1]/div"
WALLET_ONLINE_WORKERS = "/html/body/main/div[4]/div[1]/div[1]/div[1]/div/div[2]/div/p[2]/span[1]"
WALLET_OFFLINE_WORKERS = "/html/body/main/div[4]/div[1]/div[1]/div[1]/div/div[2]/div/p[2]/span[2]"
WALLET_PAYOUT_COIN = "/html/body/main/div[4]/div[1]/div[1]/div[1]/div/div[3]/div/p[2]"
WALLET_CLEARED_BALANCE = "/html/body/main/div[4]/div[1]/div[1]/div[1]/div/div[4]/div/p[2]/span/span[1]"

# Earning History
EARNING_1_DAY = ("/html/body/main/div[4]/div[1]/div[1]/div[3]/div[2]/div[1]/div/div/table/tbody/tr[1]/td["
                   "2]/span/span[1]")
EARNING_7_DAYS = ("/html/body/main/div[4]/div[1]/div[1]/div[3]/div[2]/div[1]/div/div/table/tbody/tr[2]/td["
                      "2]/span/span[1]")
EARNING_14_DAYS = ("/html/body/main/div[4]/div[1]/div[1]/div[3]/div[2]/div[1]/div/div/table/tbody/tr[3]/td["
                         "2]/span/span[1]")
EARNING_30_DAYS = ("/html/body/main/div[4]/div[1]/div[1]/div[3]/div[2]/div[1]/div/div/table/tbody/tr[4]/td["
                       "2]/span/span[1]")

# Wallet Hash-rate
HASH_RATE_5_MIN = "/html/body/main/div[4]/div[1]/div[2]/div/div[2]/div[1]/div/div[3]/table/tbody/tr/td[1]/span[1]"
HASH_RATE_1_HOUR = "/html/body/main/div[4]/div[1]/div[2]/div/div[2]/div[1]/div/div[3]/table/tbody/tr/td[2]/span[1]"
HASH_RATE_6_HOURS = "/html/body/main/div[4]/div[1]/div[2]/div/div[2]/div[1]/div/div[3]/table/tbody/tr/td[3]/span[1]"
HASH_RATE_12_HOURS = ("/html/body/main/div[4]/div[1]/div[2]/div/div[2]/div[1]/div/div[3]/table/tbody/tr/td["
                          "4]/span[1]")
HASH_RATE_24_HOURS = ("/html/body/main/div[4]/div[1]/div[2]/div/div[2]/div[1]/div/div[3]/table/tbody/tr/td["
                              "5]/span[1]")

# Workers
WORKER_1_RIG_NAME = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[1]/td[2]"
WORKER_1_HS = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[1]/td[3]/span[1]"
WORKER_1_DIFFICULTY = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[1]/td[4]"
WORKER_1_SPM = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[1]/td[5]"
WORKER_1_CONNECT_TIME = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[1]/td[6]"
WORKER_1_LAST_SEEN = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[2]/td[7]"
WORKER_1_LAST_SHARE = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[1]/td[8]"
WORKER_1_SERVER = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[1]/td[9]"
WORKER_1_TYPE = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[1]/td[10]"

WORKER_2_RIG_NAME = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[2]/td[2]"
WORKER_2_HS = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[2]/td[3]/span[1]"
WORKER_2_DIFFICULTY = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[2]/td[4]"
WORKER_2_SPM = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[2]/td[5]"
WORKER_2_CONNECT_TIME = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[2]/td[6]"
WORKER_2_LAST_SEEN = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[2]/td[7]"
WORKER_2_LAST_SHARE = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[2]/td[8]"
WORKER_2_SERVER = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[2]/td[9]"
WORKER_2_TYPE = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[2]/td[10]"

WORKER_3_RIG_NAME = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[3]/td[2]"
WORKER_3_HS = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[3]/td[3]/span[1]"
WORKER_3_DIFFICULTY = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[3]/td[4]"
WORKER_3_SPM = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[3]/td[5]"
WORKER_3_CONNECT_TIME = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[3]/td[6]"
WORKER_3_LAST_SEEN = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[3]/td[7]"
WORKER_3_LAST_SHARE = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[3]/td[8]"
WORKER_3_SERVER = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[3]/td[9]"
WORKER_3_TYPE = "/html/body/main/div[4]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[3]/td[10]"

# TODO: Payouts
