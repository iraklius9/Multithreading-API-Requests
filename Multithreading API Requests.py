import requests
import json
import threading
import time

data_list = []


def saving_information(url):
    info = requests.get(url)
    info = info.json()
    data_list.append(info)


start = time.perf_counter()
threads = []
API_LIST = []

for i in range(1, 101):
    new_api = f"https://dummyjson.com/products/{i}"
    API_LIST.append(new_api)

for api in API_LIST:
    thread = threading.Thread(target=saving_information, daemon=True, args=(api,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

with open("phones.json", "w") as file:
    json.dump(data_list, file, indent=4)

end = time.perf_counter()
print(end - start)
