import requests
import time
import random
from colorama import init, Fore, Style
from header.header import HEADERS
from delay.delay import COLLECT_COIN_DELAY_MIN, COLLECT_COIN_DELAY_MAX, RECOVER_COIN_DELAY_MIN, RECOVER_COIN_DELAY_MAX, LOOP_DELAY

# Inisialisasi colorama
init()

# Endpoints
DAILY_CHECKIN_URL = "https://api.labr.meme/api/v1/daily-rewards"
CLAIM_REWARD_URL = "https://api.labr.meme/api/v1/location/collect-reward"
COLLECT_COIN_URL = "https://api.labr.meme/api/v1/collect-coin"
RECOVER_COIN_URL = "https://api.labr.meme/api/v1/collect-coin/recover-coin"

# Banner
def print_banner():
    banner = [
        "╔══════════════════════════════════════════════╗",
        "║    🌟 LABR BOT - Automated Coin Collector    ║",
        "║  Automate your LABR account tasks with ease  ║",
        "║  Developed by: https://t.me/sentineldiscus   ║",
        "╚══════════════════════════════════════════════╝"
    ]
    for line in banner:
        print(Fore.BLUE + line + Style.RESET_ALL)

def daily_checkin():
    try:
        response = requests.get(DAILY_CHECKIN_URL, headers=HEADERS)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list):
                if len(data) > 0:
                    latest_item = max(data, key=lambda x: x.get("day", 0))
                    amount = latest_item.get("amount", {})
                else:
                    print(Fore.RED + "Daily Checkin: Respons API adalah list kosong" + Style.RESET_ALL)
                    return response.status_code
            else:
                amount = data.get("amount", {})
            log = f"Daily Checkin: Bones={amount.get('bones', 0)}, Gold={amount.get('gold', 0)}, Labr=0, Star=0, Last Login=N/A"
            print(Fore.GREEN + log + Style.RESET_ALL)
        else:
            print(Fore.RED + "Daily Checkin: Selesai" + Style.RESET_ALL)
        return response.status_code
    except requests.RequestException as e:
        print(Fore.RED + f"Daily Checkin Error: {e}" + Style.RESET_ALL)
        return None

def claim_reward():
    try:
        response = requests.post(CLAIM_REWARD_URL, headers=HEADERS)
        if response.status_code == 200:
            print(Fore.GREEN + "Claim Reward: Berhasil" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Claim Reward: Selesai" + Style.RESET_ALL)
        return response.status_code
    except requests.RequestException as e:
        print(Fore.RED + f"Claim Reward Error: {e}" + Style.RESET_ALL)
        return None

def collect_coin():
    try:
        response = requests.patch(COLLECT_COIN_URL, headers=HEADERS)
        if response.status_code == 200:
            data = response.json()
            bones = data.get("newBalance", {}).get("bones", 0)
            print(Fore.GREEN + f"Collect Coin: Bones={bones}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Collect Coin: Selesai" + Style.RESET_ALL)
        return response.status_code
    except requests.RequestException as e:
        print(Fore.RED + f"Collect Coin Error: {e}" + Style.RESET_ALL)
        return None

def recover_coin():
    try:
        response = requests.patch(RECOVER_COIN_URL, headers=HEADERS)
        if response.status_code == 200:
            print(Fore.GREEN + "Recover Coin: Berhasil" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Recover Coin: Selesai" + Style.RESET_ALL)
        return response.status_code
    except requests.RequestException as e:
        print(Fore.RED + f"Recover Coin Error: {e}" + Style.RESET_ALL)
        return None

def main():
    print_banner()
    while True:
        print("\nMenu:")
        print("1. Jalankan Daily Checkin dan Claim Reward")
        print("2. Jalankan Loop Collect Coin dan Recover Coin")
        print("0. Keluar")
        
        try:
            choice = int(input("Masukkan pilihan (1, 2, atau 0 untuk keluar): ").strip())
        except ValueError:
            print(Fore.RED + "Pilihan tidak valid. Harap masukkan angka 1, 2, atau 0." + Style.RESET_ALL)
            continue
        
        if choice == 1:
            print(Fore.GREEN + "Menjalankan Daily Checkin..." + Style.RESET_ALL)
            daily_checkin()
            time.sleep(1)
            print(Fore.GREEN + "Menjalankan Claim Reward..." + Style.RESET_ALL)
            claim_reward()
        
        elif choice == 2:
            print(Fore.YELLOW + "Memulai Loop Collect/Recover Coin (Tekan Ctrl+C untuk berhenti)..." + Style.RESET_ALL)
            try:
                while True:
                    while True:
                        status = collect_coin()
                        if status != 200:
                            break
                        time.sleep(random.uniform(COLLECT_COIN_DELAY_MIN, COLLECT_COIN_DELAY_MAX))
                    
                    while True:
                        status = recover_coin()
                        if status != 200:
                            break
                        time.sleep(random.uniform(RECOVER_COIN_DELAY_MIN, RECOVER_COIN_DELAY_MAX))
                    
                    print(Fore.YELLOW + "Loop selesai. Memulai ulang setelah 60 detik..." + Style.RESET_ALL)
                    time.sleep(LOOP_DELAY)
            except KeyboardInterrupt:
                print(Fore.YELLOW + "\nLoop Collect/Recover Coin dihentikan." + Style.RESET_ALL)
        
        elif choice == 0:
            print(Fore.GREEN + "Keluar dari program." + Style.RESET_ALL)
            break
        
        else:
            print(Fore.RED + "Pilihan tidak valid. Harap masukkan 1, 2, atau 0." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
