from cgitb import reset
import csv
import time
from tkinter import E
import requests
import json
from discord_webhook import DiscordWebhook, DiscordEmbed, webhook

headers = {
    'authority': 'backend.nftmonogatari.xyz',
    'accept': '*/*',
    'accept-language': 'nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7',
    'origin': 'https://nftmonogatari.xyz',
    'referer': 'https://nftmonogatari.xyz/',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}

with open('config.json') as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()
delay = int(jsonObject['delay'])

with open('nftmonogatari.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            time.sleep(1)
        else:
            while True:
                try:
                    line_count += 1
                    twitter = row[0]
                    address = row[1]
                except Exception as e:
                    print(e)
                else:
                    break
            while True:
                try:
                    link = f'https://backend.nftmonogatari.xyz/add-to-wl'
                    json_data = {
                        'twitter_username': f'{twitter}',
                        'wallet': f'{address}',
                    }
                    s = requests.Session()
                    response = s.post(link, data=json_data, headers=headers)
                except Exception as e:
                    print(e)
                    time.sleep(delay)
                if response.status_code == 200:
                    print(response.text)
                    time.sleep(delay)
                    break
            
