import http.client
import ssl

# ===========================================
# 🛡️ ADVANCED HEADER CHECKER - Pentester Mode
# ===========================================

target = input("🎯 Entre un site (ex: example.com) : ")

try:

    # Création d'un contexte SSL sécurisé
    context = ssl.create_default_context()

    # Connexion HTTPS au site 
    connection = http.client.HTTPConnection(target, context=context)
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

    score = 0

    # On vérifie chaque header
    for header, description in security_headers.items():

        if header in headers:
            print(f"🟢 {header} présent")
            print(f"   → {description}\n")
        else:
            print(f"🔴 {header} ABSENT")
            print("✅ Analyse terminée.")
            
    print(f"\n🎯 Score sécurisé : {score}/{len(security_headers)}")

    if score == len(security_headers):
        print("🏆 Configuration solide.")
    elif score == 3:
        print("👍 Sécurité correcte mais améliorable.")
    else:
        print("⚠️ Configuration faible.")

except Exception as e:
    print("\n❌ Erreur de connexion.")
    print("Vérifie que le site est accessible en HTTPS.")
