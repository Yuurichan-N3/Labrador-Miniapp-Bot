try:
    with open('data.txt', 'r') as file:
        token = file.read().strip()
except FileNotFoundError:
    raise Exception("File data.txt tidak ditemukan. Pastikan file ada di direktori yang sama dengan bot.py.")
except Exception as e:
    raise Exception(f"Gagal membaca data.txt: {e}")

# Prefix Bearer
authorization = f"Bearer {token}"

# Headers
HEADERS = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "authorization": authorization,
    "cache-control": "no-cache",
    "ngrok-skip-browser-warning": "true",
    "origin": "https://app.labr.meme",
    "pragma": "no-cache",
    "referer": "https://app.labr.meme/",
    "sec-ch-ua": '"Microsoft Edge";v="136", "Microsoft Edge WebView2";v="136", "Not.A/Brand";v="99", "Chromium";v="136"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}
