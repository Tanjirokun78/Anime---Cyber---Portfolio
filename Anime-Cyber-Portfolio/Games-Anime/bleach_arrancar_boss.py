import random
import time

# ====== OUTILS ======

def pause():
    input("\n⏎ Appuie sur Entrée pour continuer...")

def barre(valeur, max_val=100, taille=20):
    rempli = int((valeur / max_val) * taille)
    return "[" + "█" * rempli + "-" * (taille - rempli) + "]"

def clair():
    print("\n" * 3)

def lent(texte):
    for c in texte:
        print(c, end="", flush=True)
        time.sleep(0.05)
    print()

# ====== ARRANCAR (BOSS) ======

arrancars = {
    "Grimmjow Jaegarjaquez": {
        "type": "berserker",
        "vie": (90, 110),
        "force": (25, 40),
        "resu_chance": 5
    },
    "Ulquiorra Cifer": {
        "type": "stratège",
        "vie": (110, 140),
        "force": (20, 30),
        "resu_chance": 4
    },
    "Nnoitra Gilga": {
        "type": "rage",
        "vie": (130, 160),
        "force": (30, 45),
        "resu_chance": 6
    }
}

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

    # ===== CRÉATION ARRANCAR

    boss_nom = random.choice(list(arrancars.keys()))
    boss = arrancars[boss_nom]

    hollow_vie = random.randint(*boss["vie"])
    hollow_force_min, hollow_force_max = boss["force"]

    print(f"🔥 ARRANCAR {boss_nom.upper()} APPARAÎT !")
    print(f"PV : {hollow_vie}")
    pause()

    max_hollow_vie = hollow_vie

    # ====== COMBAT ======
    fuite = False
    while hollow_vie > 0 and vie > 0:

        clair()

        print(f"❤️ Vie : {barre(vie)} {vie}")
        print(f"🔵 Reiatsu : {barre(reiatsu)} {reiatsu}")
        print(f"⚔️ Bankai actif : {'Oui' if bankai_actif else 'Non'}")
        print(f"👹 {boss_nom}")
        print(f"💀 PV BOSS : {barre(hollow_vie, max_hollow_vie)} {hollow_vie}/{max_hollow_vie}")

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
            print(f"⚔️ Tu frappes le Arrancar Boss : -{degats} PV")

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

        # ===== RESURRECIÓN (RARE) =====

        if random.randint(1, 100) <= boss["resu_chance"]:
            clair()
            lent("🌑 L'Arrancar sourit...")
            lent("🌌 RESURRECCIÓN.")
            lent("💀 Tu es anéanti instantanément.")
            vie = 0
            break

        # ===== RIPOSTE ARRANCAR =====

        
        degats = random.randint(hollow_force_min, hollow_force_max)
        vie -= degats
        print(f"👹 Le Hollow attaque ! -{degats} PV")

            # --- Pouvoir spécial ---
        if boss["type"] == "berserker" and random.randint(1, 100) < 30:
            bonus = random.randint(10, 20)
            vie -= bonus
            print(f"💢 Attaque sauvage !")
            
        elif boss["type"] == "stratège" and random.randint(1, 100) < 25:
            reiatsu -= 15
            reiatsu = max(0, reiatsu)
            print(f"🧠 Pression spirituelle écrasante !")

        elif boss["type"] == "rage" and random.randint(1, 100) > 35:
            print(f"🩸 Le boss encaisse la douleur et frappe plus fort.")

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