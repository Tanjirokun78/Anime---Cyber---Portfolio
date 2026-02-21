import random
import time

# ========= ÉTAT DU JOUEUR =========

argent = 1000
reputation = 10
dettes = 0
tour = 1

adversaires = [
    {"nom": "Aoi", "style": "agressive"},
    {"nom": "Ririka", "style": "froide"},
    {"nom": "Itsuki", "style": "risquée"},
    {"nom": "Madari", "style": "chaotique"},
]

# ====== OUTILS ======

def pause():
    input("\n⏎ Appuie sur Entrée...")

def barre(val):
    val = max(0, min(100, val))
    plein = int(val / 10)
    return "[" + "█" * plein + "·" * (10 - plein) + "]"

def etat():
    print("\n🎓 TON STATUT")
    print(f"💰 Argent      : {argent}¥")
    print(f"👁️ Réputation  : {barre(reputation)} {reputation}%")
    print(f"⛓ Dettes      :  {dettes}¥")

# ====== INTRO ======

print("""
=====================================
🎲 GAMBLING SCHOOL
Hyakkaou Private Academy
=====================================
Ici, le talent ne suffit pas.
Seuls les joueurs survivent.
""")
pause()

# ====== BOUCLE PRINCIAPLE ======

while True:
    print(f"\n🔁 Tour {tour}")
    etat()

    if argent <= 0:
        print("\n💀 Tu es ruiné.")
        print("Tu deviens un animal dosmestique de l'école 😔.")
        break

    if reputation >= 100:
        print("\n👑 Toute l'école te craint.")
        print("Tu es au sommet ! ")
        break

    adversaire = random.choice(adversaires)
    print(f"\n🃏 Duel proposé par {adversaire['nom']} ({adversaire['style']})")

    print("""
Actions :
[1] Accepter le duel
[2] Refuser (perte de réputation)
[3] Miser gros (haut risque)
[4] Quitter l'école
""")
    
    choix = input("➡ ").strip()

    if choix == "4":
        print("\nTu quittes l'école vivant...pour l'instant.")
        break
    
    if choix == "2":
        reputation -= 10
        print("😶 Tu refuses. Ta réputation chute.")
        tour += 1 
        continue

    mise = random.randint(100, 400)

    if choix == "3":
        mise *= 2
        print(f"🔥 Tu mises énormément : {mise}¥")

    else:
        print(f"🎲 Mise standard : {mise}¥")

    pause()
    print("\nLe jeu commence...")
    time.sleep(1)

    chance_joueur = random.randint(1, 100) + reputation
    chance_adv = random.randint(1, 100)

    # Style adverses
    if adversaire["style"] == "agressive":
        chance_adv += 15
    elif adversaire["style"] == "froide":
        chance_adv += 5
    elif adversaire["style"] == "chaotique":
        chance_adv += random.randint(-20, 30)
    
    if chance_joueur > chance_adv:
        argent += mise
        reputation += random.randint(8, 15)
        print(f"💥 VICTOIRE ! Tu gagnes {mise}¥")
    else:
        argent -= mise
        dettes += mise // 2
        reputation -= random.randint(5, 10)
        print(f"💀 DÉFAITE...Tu perds {mise}¥")

    tour += 1
    time.sleep(0.8)

# ====== FIN ======

print("\n🎭 FIN DE PARTIE")
print(f"Tours joués : {tour}")
print("L'école n'oublie jamais.")
