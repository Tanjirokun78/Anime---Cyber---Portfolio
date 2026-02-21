url = input("🌐 Entrée l'url à vérifier : ").strip()
suspects_world = ["login", "verify", "account", "secure"]
if any(word in url.lower() for word in suspects_world):
    print("⚠️ Attention : cette URL semble suspecte 🫆 !")
else:
    print("✅ URL probablement sûre 😊")