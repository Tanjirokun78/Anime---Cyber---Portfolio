import re 
from collections import Counter

print("""
\033[38;2;255;255;255m ____  _    _   _ _____   _____ _____    _    __  __ \033[0m               
\033[38;2;255;210;210m| __ )| |  | | | | ____| |_   _| ____|  / \  |  \/  |\033[0m               
\033[38;2;255;210;210m|  _ \| |  | | | |  _|     | | |  _|   / _ \ | |\/| |\033[0m  _____        
\033[38;2;255;180;180m| |_) | |__| |_| | |___    | | | |___ / ___ \| |  | | |_____|\033[0m       
\033[38;2;255;180;180m|____/|_____\___/|_____|  _|_|_|_____/_/___\_\_|_ |_|_  _____ ____\033[0m  
\033[38;2;255;130;130m| |   / _ \ / ___| |  _ \| ____|  ___| ____| \ | |  _ \| ____|  _ \\\033[0m 
\033[38;2;255;130;130m| |  | | | | |  _  | | | |  _| | |_  |  _| |  \| | | | |  _| | |_) |\033[0m
\033[38;2;255;90;90m| |__| |_| | |_| | | |_| | |___|  _| | |___| |\  | |_| | |___|  _ <\033[0m 
\033[38;2;200;0;0m|_____\___/ \____| |____/|_____|_|   |_____|_| \_|____/|_____|_| \_\\
""")

file_path = input("📂 Chemin du ficher log : ")

try:
    with open(file_path, "r") as file:
        logs = file.readlines()
except:
    print("❌ Impossible d'ouvrir le fichier.")
    exit()

failed_attempts = []
ip_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"

# ==============================
# ANALYSE DES LOGS
# ==============================

for line in logs:
    if "Failed" in line or "failed" in line:
        ip_match = re.search(ip_pattern, line)
        if ip_match:
            failed_attempts.append(ip_match.group())

# ==============================
# ANALYSE IP SUSPECTES
# ==============================

ip_count = Counter(failed_attempts)

print("\n🚨 Résultats :\n")

for ip, count in ip_count.items():
    if count >= 3:
        print(f"🔴 IP suspecte: {ip} ({count} tentatives)")
    else:
        print(f"🟡 Ip à surveiller : {ip} ({count} tentatives)")

if not ip_count:
    print("✅ Aucun comportement suspect détecté.")

print("\n🛡️ Analyse terminée.")