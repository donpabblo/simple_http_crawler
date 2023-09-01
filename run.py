import requests
import os
import platform
import time
import json
import subprocess
import random
import logging
from configparser import ConfigParser

config_object = ConfigParser()
config_object.read("config.ini")
sheet_url = config_object["SHEET"]["url"]
print("Sheet URL is {}".format(sheet_url))
iter_wait_time = config_object["APP"]["wait_time"]
print("Iteration wait time is {} minutes".format(iter_wait_time))
speedify_wait_time = config_object["SPEEDIFY"]["wait_time"]
print("Speedify wait time is {} minutes".format(speedify_wait_time))
speedify_path = config_object["SPEEDIFY"]["path"]
print("Speedify path is {}".format(speedify_path))
speedify_country = config_object["SPEEDIFY"]["country"]
print("Speedify country is {}".format(speedify_country))
rotate_ip_param = config_object["APP"]["rotate_ip"]
print("Rotate ip {}".format(rotate_ip_param))
min_wait_time = config_object["APP"]["min_wait"]
print("Min wait time is {}".format(min_wait_time))
max_wait_time = config_object["APP"]["max_wait"]
print("Max wait time is {}".format(max_wait_time))

logging.basicConfig(filename='app.log', encoding='utf-8', level=logging.DEBUG)

def rotate_ip():
    try:
        if platform.system() == 'Windows':
            servers = subprocess.run([speedify_path, 'show', 'servers'], capture_output=True, text=True).stdout
            public_servers = (json.loads(servers))['public']
            filtered_servers = [p for p in public_servers if p['country'] == speedify_country]
            random_server = random.choice(filtered_servers)
            print("Connecting to {}".format(random_server['tag']))
            logging.info("Connecting to {}".format(random_server['tag']))
            connection_output = subprocess.run([speedify_path, 'connect', random_server['country'], random_server['city'], str(random_server['num'])], capture_output=True, text=True).stdout
            print("Now my IP is: {}".format((json.loads(connection_output))['publicIP']))
            logging.info("Now my IP is: {}".format((json.loads(connection_output))['publicIP']))
        elif platform.system() == 'Linux':
            os.system('ls')
        else:
            print("You are on a MAC, unable to rotate IP")
            logging.info("You are on a MAC, unable to rotate IP")
    except Exception as error:
        print("An exception occurred:", error)
        logging.error("An exception occurred:", error)
    finally:
        time.sleep(int(speedify_wait_time))

def main():
    try:
        while True:
            if rotate_ip_param == 'true':
                rotate_ip();
            print("Getting urls from {}".format(sheet_url))
            logging.info("Getting urls from {}".format(sheet_url))
            response = requests.get(sheet_url)
            response_json = response.json()
            random.shuffle(response_json['data'])
            for item in response_json['data']:
                print("Loading {}".format(item['url']))
                logging.info("Loading {}".format(item['url']))
                http_call = requests.get(item['url'], headers={"authority": "www.vinted.it", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "accept-language": "it,en;q=0.9,it-IT;q=0.8,en-US;q=0.7,la;q=0.6,fr;q=0.5", "cache-control": "max-age=0", "referer": "https://www.vinted.it/", "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                wait_time = random.randrange(int(min_wait_time), int(max_wait_time))
                print("Waiting {} seconds".format(wait_time))
                logging.info("Waiting {} seconds".format(wait_time))
                time.sleep(wait_time)
            time.sleep(int(iter_wait_time))
    except Exception as error:
        print("An exception occurred:", error)
        logging.error("An exception occurred:", error)
        
if __name__ == '__main__':
    main()
