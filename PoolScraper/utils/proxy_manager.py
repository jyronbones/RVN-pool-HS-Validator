import re


def read_proxies(filename):
    scheme = 'http'
    proxies = []
    with open(filename) as file:
        for line in file:
            pr = line.strip()
            m = re.search(r'(.*):(.*):(.*):(.*)', pr)
            if m:
                # Format for seleniumwire: 'username:password@host:port'
                proxy = f"{m.group(3)}:{m.group(4)}@{m.group(1)}:{m.group(2)}"
                proxies.append(proxy)
    return proxies
