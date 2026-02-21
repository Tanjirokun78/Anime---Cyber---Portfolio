import socket
import ssl
import whois
from datetime import datetime

# ==========================================
# 🧠 MINI OSINT TOOL - DOMAIN RECON
# ==========================================

print("🕵️ OSINT DOMAIN RECON TOOL\n")

# on demande un domaine à analyser
domain = input("🎯 Entre un domaine (ex: example.com) : ")

print("\n🔎 PHASE 1 - Résolution DNS")
try:
    # on transforme le nom de domaine en adresse IP
    ip = socket.gethostbyname(domain)
    print(f"🌍 Adresse IP : {ip}")
except:
    print("❌ Impossible de résoudre le domaine.")
    exit()

print("\n📜 PHASE 2 - Informations WHOIS")
try:
    # on récupère les informations publique du domaine
    domain_info = whois.wohis(domain)

    print(f"📅 Date de création : {domain_info.creation_date}")
    print(f"📅 Date d'expiration : {domain_info.expiration_date}")
    print(f"🏢 Registrar : {domain_info.registrar}")
except:
    print("⚠️ Impossible de récupèrer les infos WHOIS.")

print("\n🔐 Phase 3 - Analyse du certificat SSL")

try:
    # création d'un contexte SSL
    context = ssl.create_default_context()

    # connexion au serveur sur le port HTTPS (443)
    with socket.create_connection((domain, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:

            # récupération du certificat
            cert = ssock.getpeercert()

            print("🔑 Certificat SSL valide.")

            # on affiche la date d'expiration du certificat
            expiry_date = cert['notAfter']
            print(f"📅 Expiration du certificat : {expiry_date}")

except:
    print("⚠️ Pas de certificat SSL détecté ou erreur HTTPS.")

print("\n✅ Analyse OSINT terminée 😊 .")