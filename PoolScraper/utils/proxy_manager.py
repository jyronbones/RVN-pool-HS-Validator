import random
import re


class ProxyManager:
    def __init__(self, filename):
        self.proxies = self._read_proxies(filename)

    @staticmethod
    def _read_proxies(filename):
        proxies = []
        with open(filename) as file:
            for line in file:
                pr = line.strip()
                m = re.search(r'(.*):(.*):(.*):(.*)', pr)
                if m:
                    proxy = f"{m.group(3)}:{m.group(4)}@{m.group(1)}:{m.group(2)}"
                    proxies.append(proxy)
        return proxies

    def get_random_proxy(self):
        return random.choice(self.proxies) if self.proxies else None
