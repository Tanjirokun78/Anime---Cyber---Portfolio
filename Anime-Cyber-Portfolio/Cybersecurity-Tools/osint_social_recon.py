import requests
import time
import sys

def loading(text):
    for i in range(3):
        sys.stdout.write(f"\r{text}{'.' * i}")
        sys.stdout.flush()
        time.sleep(0.5)

loading("🔎 Initialisation du module OSINT")
print("\n🟢 Module chargé.")

banner = """
\033[38;2;255;255;255m  ___  ____ ___ _   _ _____   ____  _____ ____ ___  _   _     ______   __\033[0m
\033[38;2;255;210;210m / _ \\/ ___|_ _| \\ | |_   _| |  _ \\| ____/ ___/ _ \\| \\ | |   |  _ \\ \\ / /\033[0m
\033[38;2;255;130;130m| | | \\___ \\| ||  \\| | | |   | |_) |  _|| |  | | | |  \\| |   | |_) \\ V /\033[0m
\033[38;2;255;90;90m| |_| |___) | || |\\  | | |   |  _ <| |__| |__| |_| | |\\  |  _|  __/ | |\033[0m  
\033[38;2;200;0;0m \\___/|____/___|_| \\_| |_|   |_| \\_\\_____\\____\\___/|_| \\_| (_)_|    |_|\033[0m  
"""
print(banner)
pseudo = input("🎯 Entre le pseudo à tester : ").strip()

# liste des plateformes et leurs URLs de profil
platforms = {
    "Twitter": f"https://twitter.com/{pseudo}",
    "Instagram": f"https://www.instagram.com/{pseudo}",
    "GitHub": f"https://github.com/{pseudo}",
    "Reddit": f"https://www.reddit.com/user/{pseudo}",
    "TikTok": f"https://www.tiktok.com/@{pseudo}",
    "YouTube": f"https://www.youtube.com/{pseudo}",
}

results = {}

print("\n🔍 Vérification des pseudos...\n")
for name, url in platforms.items():
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            results[name] = ("Exist", url)
            print(f"🟢 {name} → Compte trouvé ! ({url})")
        else:
            results[name] = ("Not Found", url)
            print(f"🔴 {name} → Pas de compte trouvé")
    except:
        results[name] = ("Error", url)
        print(f"⚠️ {name} → Erreur de connexion")

print("\n📊 Résumé OSINT:\n")
for name, info in results.items():
    status, url = info
    print(f"{name}: {status} {(url)}")