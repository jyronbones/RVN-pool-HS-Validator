import pyodbc


class DatabaseManager:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.conn = None
        self.cursor = None

    def connect(self):
        if not self.conn or not self.cursor:
            self.conn = pyodbc.connect(self.connection_string)
            self.cursor = self.conn.cursor()

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
            self.cursor = None
        if self.conn:
            self.conn.close()
            self.conn = None

    def insert_wallet_stats(self, wallet_stats):
        try:
            self.connect()
            query = """INSERT INTO WalletStats (HashRate, OnlineWorkers, OfflineWorkers, PayoutCoin, ClearedBalance) 
                       VALUES (?, ?, ?, ?, ?);"""
            self.cursor.execute(query, wallet_stats)
            self.conn.commit()
        finally:
            self.disconnect()

    def insert_earning_history(self, earning_history):
        try:
            self.connect()
            query = """INSERT INTO EarningHistory (OneDay, SevenDays, FourteenDays, ThirtyDays) 
                       VALUES (?, ?, ?, ?);"""
            self.cursor.execute(query, earning_history)
            self.conn.commit()
        finally:
            self.disconnect()

    def insert_hash_rates(self, hash_rates):
        try:
            self.connect()
            query = """INSERT INTO HashRates (FiveMin, OneHour, SixHours, TwelveHours, TwentyFourHours) 
                       VALUES (?, ?, ?, ?, ?);"""
            self.cursor.execute(query, hash_rates)
            self.conn.commit()
        finally:
            self.disconnect()

    def insert_worker_data(self, worker):
        try:
            self.connect()
            query = """INSERT INTO Workers (RigName, Hashrate, Difficulty, SPM, ConnectTime, LastSeen, LastShare, Server, Type) 
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"""
            self.cursor.execute(query, (
                worker['rig_name'],
                worker['hashrate'],
                worker['difficulty'],
                worker['spm'],
                worker['connect_time'],
                worker['last_seen'],
                worker['last_share'],
                worker['server'],
                worker['type']
            ))
            self.conn.commit()
        finally:
            self.disconnect()
