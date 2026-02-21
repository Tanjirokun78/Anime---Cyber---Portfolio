import re 
from collections import Counter
import datetime

print("""
\033[38;2;173;216;230m ____  _    _   _ _____  __        ___  _____ ____ _   _\033[0m
\033[38;2;120;280;220m| __ )| |  | | | | ____| \\ \\      / / \\|_   _/ ___| | | |\033[0m
\033[38;2;70;130;180m|  _ \\| |  | | | |  _|    \\ \\ /\\ / / _ \\ | || |   | |_| |\033[0m
\033[38;2;30;90;150m| |_) | |__| |_| | |___    \\ V  V / ___ \\| || |___|  _  |\033[0m
\033[38;2;0;40;120m|____/|_____\\___/|_____|    \\_/\\_/_/   \\_\\_| \\____|_| |_|\033[0m
""")

file_path = input("📂 Chemin du fichier log : ")

try:
    with open(file_path, "r") as file:
        logs = file.readlines()
except:
    print("❌ Impossible d'ouvrir le fichier.")
    exit()

ip_patterns = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
failed_ips = []
admin_attempts = 0
night_activity = 0

# ==============================
# ANALYSE
# ==============================

for line in logs:

    # détection échec login
    if "Failed" in line:
        ip_match = re.search(ip_patterns, line)
        if ip_match:
            failed_ips.append(ip_match.group())

    # tentative admin
    if "admin" in line.lower():
        admin_attempts += 1

    # activité nocturne (ex: 02:14:33)
    time_match = re.search(r"\b([01]?\d|2[0-3]):[0-5]\d:[0-5]\d\b", line)
    if time_match:
        hour = int(time_match.group().split(":")[0])
        if hour >= 0 and hour <= 5:
            night_activity += 1

# ==============================
# SCORING
# ============================== 

ip_count = Counter(failed_ips)
threat_score = 0

for ip, count in ip_count.items():
    if count >= 5:
        threat_score += 3
    elif count >= 3:
        threat_score += 2
    else:
        threat_score += 1

threat_score += admin_attempts * 2
threat_score += night_activity

# ==============================
# CLASSIFICATION
# ==============================

print("\n📊 Threat Analysis Report\n")

if threat_score <= 3:
    level = "🟢 NORMAL"
elif threat_score <= 7:
    level = "🟡 SUSPICIOUS"
else:
    level = "🔴 HIGH RISK"

print(f"Threat Score : {threat_score}")
print(f"Classification : {level}")
print(f"Admin Attempts : {admin_attempts}")
print(f"Night Activity : {night_activity}")
print(f"Unique Failed IPs : {len(ip_count)}")

print("\n🛡️ Analysis complete.")