import random
import time

def lent(text, delay=0.03):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()

def pause():
    input("\n⏎ Appuie sur Entrée pour continuer...")

def clair():
    print("\n" * 2)

# ====== INTRO ======
clair()
lent("🧬 CYBER ACADEMY - Simulation Phishing\n", 0.05)
lent("Tu vas recevoir plusieurs emails.\n")
lent("Ton objectif : détecter lesquels sont des tentatives de phishing.\n")
pause()

score = 0

emails = [
{
"contenu": """
📧 De : security-paypal@secure-update.com
Objet : URGENT - Votre compte sera suspendu

Cher client, 

Une activité suspecte a été détectée sur votre compte.
Veuillez vous connecter immédiatement pour vérifier vos informations :

http://paypal-verification-secure-login.com

Merci, 
Service Sécurité
""",
"phishing": True
},
{
"contenu": """
📧 De : no-reply@netflix.com
Objet : Votre facture mensuelle 

Bonjour, 

Votre abonnement Netflix a été renouvelé avec succès.
Montant : 13,99€

Merci de votre fidélité.
""",
"phishing": False
},
{
"contenu": """
📧 De : admin@micro0soft-support.com
Objet : Problème critique détecté

Votre ordinateur est infecté.
Téléchargez immédiatement le correctif ici :

htpp//fix-security-now.ru
""",
"phishing": True
}
]

random.shuffle(emails)

for i, email in enumerate(emails, 1):
    clair()
    lent(f"📨 Email {i} reçu :\n", 0.04)
    print(email["contenu"])

    choix = input("\n⚠️ Cet email est-il du phishing ? (oui/non) : ").lower().strip()

    if (choix == "oui" and email["phishing"]) or (choix == "non" and not email["phishing"]):
        lent("✅ Bonne réponse !")
        score += 1
    else:
        lent("❌ Mauvaise réponse.")
        if email["phishing"]:
            lent("Indices : URL suspecte, fautes, domaine étrange.")
        else:
            lent("Indices : domaine officiel et aucun lien suspect.")

    pause()

# ====== RÉSULTAT ======
clair()
lent("🎯 Simulation terminée.\n")

if score == len(emails):
    lent("🏆 Expert anti-phishing ! Tu ne te ferais pas avoir.")
elif score >= 2:
    lent("👍 Bon réflexe, mais reste vigilant.")
else:
    lent("⚠️ Attention ! Tu serais une cible facile.")

lent(f"\nScore final : {score}/{len(emails)}")