import http.client

# ==========================================
# 🛡️ MINI OUTIL PENTEST - HEADER CHECKER
# ==========================================

# On demande la cible 
target = input("🎯 Entre un site (ex: example.com) : ")

# Connexion HTTPS au site 
# (on suppose que le site utilise HTTPS)
connection = http.client.HTTPConnection(target)

# On envoie une requête GET à la racine du site
connection.request("GET", "/")

# On récupère la réponse du serveur
response = connection.getresponse()

# On récupère tous les headers sous forme de dictionnaire 
headers = dict(response.getheaders())

print("\n🔎 Analyse des headers de sécurité...\n")

# Liste des headers importants à vérifier 
security_headers = {
    "X-Frame-Options": "Protège contre le clickjacking",
    "Content-Security-Policy": "Protège contre les attaques XSS",
    "Strict-Transport-Security": "Force l'utilisation de HTTPS",
    "X-Content-Type-Options": "Empêche certains types d'attaques MIME",
    "Referrer-Policy": "Contrôle les informations envoyées en referrer"
}

# On vérifie chaque header
for header, description in security_headers.items():

    if header in headers:
        print(f"🟢 {header} présent")
        print(f"   → {description}\n")
    else:
        print(f"🔴 {header} ABSENT")
        print(f"   ⚠️ {description}\n")

print("✅ Analyse terminée.")