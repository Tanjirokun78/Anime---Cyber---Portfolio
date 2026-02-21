import random

# ====== OUTILS ======

def pause():
    input("\n⏎ Appuie sur Entrée pour continuer...")

def barre(valeur, max_val=100, taille=20):
    rempli = int((valeur / max_val) * taille)
    return "[" + "█" * rempli + "-" * (taille - rempli) + "]"

def clair():
    print("\n" * 3)

# ====== INTRO ======

print("""
=====================================
⚔️ BLEACH – CHASSEUR DE HOLLOWS
=====================================
Protège le monde des vivants.
Purifie les Hollows.
Maîtrise ton Reiatsu.
""")

pause()

# ====== JOUEUR ======

vie = 100
reiatsu = 100
bankai_actif = False
tour = 1
MAX_TOURS = 8

# ====== BOUCLE ======

while vie > 0 and tour <= MAX_TOURS:

    clair()

    # Création Hollow
    hollow_vie = random.randint(60, 120)
    hollow_force = random.randint(10, 25)

    print(f"👹 Un Hollow apparaît ! (PV : {hollow_vie})")
    pause()

    # ====== COMBAT ======
    fuite = False
    while hollow_vie > 0 and vie > 0:

        clair()

        print(f"❤️ Vie : {barre(vie)} {vie}")
        print(f"🔵 Reiatsu : {barre(reiatsu)} {reiatsu}")
        print(f"⚔️ Bankai actif : {'Oui' if bankai_actif else 'Non'}")

        print("""
Actions :
[1] Attaque Zanpakuto
[2] Technique spirituelle
[3] Activer Bankai
[4] Se concentrer (récupérer Reiatsu)
[5] Prendre la fuite...
""")
        
        choix = input("➡ Ton choix : ").strip()

        # ===== ATTAQUE BASIQUE =====

        if choix == "1":
            degats = random.randint(15, 25)

            if bankai_actif:
                degats *= 2

            hollow_vie -= degats
            print(f"⚔️ Tu frappes le Hollow : -{degats} PV")

        # ===== TECHNIQUE =====

        elif choix == "2":
            
            if reiatsu >= 25:
                degats = random.randint(30, 50)
                reiatsu -= 25
                hollow_vie -= degats
                print(f"💥 Technique spirituelle ! -{degats} PV")
            else:
                print("❌ Pas assez de Reiatsu.")

        # ===== BANKAI =====

        elif choix == "3":

            if reiatsu >= 40 and not bankai_actif:
                bankai_actif = True
                reiatsu -= 40
                print("🌌 BANKAI ACTIVÉ !!!")
            else:
                print("❌ Impossible d'activer ton Bankai.")

        # ===== CONCENTRATION =====

        elif choix == "4":
            gain = random.randint(20, 35)
            reiatsu += gain
            reiatsu = min(100, reiatsu)
            print(f"🌀 Tu récupères {gain} Reiatsu.")

        elif choix == "5":
            print("💨 Tu prends la fuite , et tu repars dans la Soul Society...")
            fuite = True
            break
        else:
            print("❌ Action invalide.")
            continue

        # ===== RIPOSTE HOLLOW =====

        if hollow_vie > 0:
            degats = random.randint(10, hollow_force)
            vie -= degats
            print(f"👹 Le Hollow attaque ! -{degats} PV")

        pause()

    # ===== FIN COMBAT =====

    if fuite:
        print("⚠️ Mission abandonnée.")
        tour += 1
        bankai_actif = False
        break

    elif vie > 0:
        print("✨ Hollow purifié.")
        reiatsu += 15
        reiatsu = min(100, reiatsu)
        tour += 1
        bankai_actif = False
        print(f"🌀 +15 Reiatsu | ⭐️ Expérience gagnée :) ")
        pause()
    

# ===== FIN =====

clair()

if vie <= 0:
    print("💀 Tu es tombé au combat...")

else:
    print("🏆 Mission accomplie Shinigami !")

print("\nMerci d'avoir joué ⚔️")