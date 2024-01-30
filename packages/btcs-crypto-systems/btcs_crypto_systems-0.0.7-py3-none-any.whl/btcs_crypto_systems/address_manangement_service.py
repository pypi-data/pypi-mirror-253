import requests
from dataclasses import dataclass, field
import time

@dataclass
class AMS:
    env:str = "test"
    base_url:str = field(init=False)

    def __post_init__(self):
        self.base_url = f"https://ams.btcs{self.env}.net/api/AddressManagement"

    def get_addresses(self, account, blockchain_id=None, include_balances=False, limit=10000000000):
        page = 0
        page_size = 100
        total = 0
        take_now = page_size
        addresses = []

        while True:
            try:
                # respect the limit
                if limit - (total + page_size*page) <= 0:
                    break
                elif limit - (total + page_size*page) < page_size:
                    take_now = limit - (total + page_size*page)
                url = ""
                if blockchain_id:
                    url = "{}/addresses?Skip={}&Take={}&AccountRef={}&BlockchainId={}&IncludeBalances={}".format(self.base_url, page*take_now, take_now, account, blockchain_id, include_balances)
                else:
                    url = "{}/addresses?Skip={}&Take={}&AccountRef={}&IncludeBalances={}".format(self.base_url, page*take_now, take_now, account, include_balances)
                response = requests.request("GET", url)
                addresses_res = response.json()
                addresses.extend(addresses_res)
                page += 1
                total += take_now
                print(f"collected {total} addresses...")
                if len(addresses_res) == 0:
                    break

            except:
                print("Error with URL: {}".format(url))
        
        return addresses
    

if __name__ == "__main__":
    ams = AMS("test")
    print(ams.get_addresses(account="1065010", limit=10))