
import requests
import random
import time
import os
from colorama import Fore
os.system ('clear')

print("=========================================================")
print("  _   _  _ _  _   _  __    ___  _  ___ _  _  _  _ ")
print(" | \_/ || U || \_/ ||  \  | __|/ \|_ _/ \| \| || |")
print(" | \_/ ||   || \_/ || o ) | _|| o || ( o ) \\ || | ")
print(" |_| |_||_n_||_| |_||__/  |_| |_n_||_|\_/|_|\_||_| ")
print("")
print('       PERINGATAN : AJA ORA KELINGAN TURU ')
print("=========================================================")
print("")
print("")
print("")
channel_id = input("Panjingi id channel: ")
waktu1 = int(input("klik 0 bae : "))
waktu2 = int(input("kien waktu ngirim pesan: "))
print("=================================================")

os.system('cls' if os.name == 'nt' else 'clear')

with open("pesan.txt", "r") as f:
    words = f.readlines()

with open("token.txt", "r") as f:
    authorization = f.readline().strip()

while True:
        channel_id = channel_id.strip()

        payload = {
            'content': random.choice(words).strip()
        }

        headers = {
            'Authorization': authorization
        }

        r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
        print(Fore.WHITE + "Sent message: ")
        print(Fore.YELLOW + payload['content'])

        response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)

        if response.status_code == 200:
            messages = response.json()
            if len(messages) == 0:
                is_running = False
                break
            else:
                time.sleep(waktu2)
