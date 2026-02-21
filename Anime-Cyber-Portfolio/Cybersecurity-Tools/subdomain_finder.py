import socket

# ==========================================
# 🕵️  MINI OUTIL PENTEST - SUBDOMAIN FINDER
# ==========================================

# Liste de sous-domaines courants utilisés par les entreprises
subdomains = [
    "www",
    "mail",
    "ftp",
    "admin",
    "test",
    "dev",
    "api",
    "blog",
    "vpn"
]

# On demande à l'utilisateur la cible
domain = input("🎯 Entre un domaine cible (ex: example.com) : ")

print("\n🔎 Recherche des sous-domaines...\n")

# Pour chaque sous-domaine dans la liste
for sub in subdomains:

    # contruction de l'adresse complète
    # Exemple : admin + example.com → admin.example.com
    full_domain = f"{sub}.{domain}"

    try:
        # On tente de résoudre le domaine en adresse IP
        # Si ça fonctionne → le sous-domaine existe
        ip = socket.gethostbyname(full_domain)

        print(f"🟢 Trouvé : {full_domain} → {ip}")

    except socket.gaierror:
        # Si ça échoue → le sous-domaine n'existe pas
        print(f"🔴 {full_domain} n'existe pas")

print("\n✅ Scan terminé.")