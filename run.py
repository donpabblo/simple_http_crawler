import requests
import time
import random
import logging
from configparser import ConfigParser

config_object = ConfigParser()
config_object.read("config.ini")
print({section: dict(config_object[section]) for section in config_object.sections()})
logging.basicConfig(filename='app.log', encoding='utf-8', level=logging.INFO)

def main():
    try:
        while True:
            myip = requests.get('http://icanhazip.com')
            print("My IP is {}".format(myip.content))
            logging.info("My IP is {}".format(myip.content))
            print("Getting urls from {}".format(config_object["APP"]["sheet_url"]))
            logging.info("Getting urls from {}".format(config_object["APP"]["sheet_url"]))
            response = requests.get(config_object["APP"]["sheet_url"])
            response_json = response.json()
            random.shuffle(response_json['data'])
            for item in response_json['data']:
                print("Loading {}".format(item['url']))
                logging.info("Loading {}".format(item['url']))
                requests.get(item['url'], headers={"authority": "www.vinted.it", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "accept-language": "it,en;q=0.9,it-IT;q=0.8,en-US;q=0.7,la;q=0.6,fr;q=0.5", "cache-control": "max-age=0", "referer": "https://www.vinted.it/", "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                wait_time = random.randrange(int(config_object["APP"]["min_wait"]), int(config_object["APP"]["max_wait"]))
                print("Waiting {} seconds".format(wait_time))
                logging.info("Waiting {} seconds".format(wait_time))
                time.sleep(wait_time)
            time.sleep(int(config_object["APP"]["wait_time"]))
    except Exception as error:
        print("An exception occurred:", error)
        logging.error("An exception occurred:", error)
        
if __name__ == '__main__':
    main()
