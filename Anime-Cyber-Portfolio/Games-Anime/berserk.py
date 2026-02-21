import random
import time

# ===== OUTILS =====

def lent(txt, vitesse=0.04):
    for c in txt:
        print(c, end="", flush=True)
        time.sleep(vitesse)
    print()

def pause():
    input("\n⏎ Appuie sur Entrée...")

def barre(val, max_val=100, size=20):
    fill = int((val / max_val) * size)
    return "[" + "█" * fill + "-" * (size - fill) + "]"

def clair():
    print("\n" * 4)

# ===== INTRO =====

clair()
print("========================================")
print("🩸 BERSERK - LA NUIT DES DAMNÉS")
print("========================================")
lent("La nuit tombe.")
lent("La Marque du Sacrifice brûle.")
lent("Ils arrivent.")
pause()

# ===== GUTS =====

vie = 120
endurance = 100
rage = 0
tour = 1
MAX_NUITS = 5

# ===== APÔTRES =====

apotres = [
    {"nom" : "Apostle du Pendu", "vie": 80, "force": (15, 25), "horreur": 10},
    {"nom" : "Apostle du Charnier", "vie": 100, "force": (20, 30), "horreur": 15},
    {"nom" : "Apostle du Vide", "vie": 120, "force": (25, 35), "horreur": 20},
    
]
ZODD_CHANCE = 0.5

GOD_HAND_CHANCE = 0.3 # 0.3% par nuit (ultra rare)

god_hand = [
    "Void",
    "Slan",
    "Ubik",
    "Conrad",
    "Femto"
]
FEMTOM_CHANCE = 0.08  # 0.08% - extrêmement rare 

# ===== BOUCLE PRINCIPALE =====

while tour <= MAX_NUITS and vie > 0:

    clair()
    lent(f"🌑 La NUIT {tour}")
    lent("La Marque saigne...")
    rage += 5
    pause()

    # ===== APPARITION DE ZODD (TRÈS RARE) =====

    if random.uniform(0, 100) < ZODD_CHANCE:
        clair()
        lent("🐂 Une présence écrasante descend du ciel...")
        time.sleep(1)
        lent("ZODD L'IMMORTEL")
        time.sleep(1)
        lent("« Tu es encore en vie ? Intéressant... »")
        pause()
        lent("💀 En un battement de cœur, tout s'arrête.")
        vie = 0
        break

    # ===== APPARITION GOD HAND ===== 

    if random.uniform(0, 100) < GOD_HAND_CHANCE:
        clair()
        membre = random.choice(god_hand)

        lent("🌌 L'espace se fissure...")
        time.sleep(1)
        lent("👁️ Des silhouettes apparaissent.")
        time.sleep(1)
        lent(f"La GOD HAND - {membre}")
        pause()

        lent("« La causalité t'a mené ici. »")
        pause()

        # Effets aléatoires
        effet = random.choice(["souffrance", "tentation", "marque"])

        if effet == "souffrance":
            lent("💀 Ton corps se tord sous une douleur divine.")
            vie -= random.randint(20, 40)
            rage += 20

        elif effet == "tentation":
            lent("😈 Une promesse te traverse l'esprit...")
            lent("« Abandonne ton humanité. »")
            pause()
            choix = input("Accepter ? (o/n) : ").lower()

            if choix == "o":
                lent("🩸 Tu as choisi le pouvoir, +50 rage +30 vie.")
                lent("Mais quelque chose en toi est mort.")
                rage += 50
                vie += 30
            else:
                lent("🔥 Tu refuses.")
                lent("La GOD HAND observe... amusée. +10 rage")
                rage += 10
        
        elif effet == "marque":
            lent("🩸 La Marque brûle comme jamais. +30 rage")
            rage += 30

        pause()

        if vie <= 0:
            lent("💀 Ton existence est effacée...")
            break
    
    # ===== FIN SECRÈTE : FEMTO =====

    if random.uniform(0, 100) < FEMTOM_CHANCE:
        clair()
        lent("🌑 Le monde devient silencieux.")
        time.sleep(1.5)

        lent("Un battement d'ailes.")
        time.sleep(1)

        lent("👁️ Un regard.")
        time.sleep(1)

        lent("Femto")
        pause()

        lent("« Tout s'est déroulé selon la causalité. »")
        time.sleep(1)

        # 👁️ FIN ALTERNATIVE SELON LA RAGE
        if rage >= 90:
            lent("🩸 Tu souris...")
            time.sleep(1)
            lent("Quelque chose en toi a accepté.")
            time.sleep(1)
            lent("Le Sacrifice n'était pas une contrainte.")
        else:
            lent("Tu comprends.")
            time.sleep(1)
            lent("Tu n'étais jamais destiné à gagner.")
        pause()

        clair()
        print("""
█████████████████████████████████
        FIN SECRÈTE
        LA CAUSALITÉ
█████████████████████████████████
              
Tu as vu Femto.
Et pourtant... rien ne s'est passé.

Ou peut-être que tout est déjà fini.
""")
        
        pause()
        break

    boss = random.choice(apotres)
    boss_vie = boss["vie"]
    boss_max = boss_vie

    lent(f"👹 {boss['nom']} apparaît.")
    pause()

    # ===== COMBAT =====

    while boss_vie > 0 and vie > 0:
        clair()
        print(f"❤️ Vie : {barre(vie, 120)} {vie}")
        print(f"💪🏽 Endurance : {barre(endurance)} {endurance}")
        print(f"🔥 Rage : {barre(rage)} {rage}")
        print(f"👹 {boss['nom']} : {barre(boss_vie, boss_max)} {boss_vie}")

        print("""
Actions :
[1] Frappe de Dragonslayer
[2] Tir du canon bras
[3] Lâcher la rage
[4] Endurer (défense)
""")
        
        choix = input("➡ Ton choix : ").strip()

        # ===== ATTAQUES =====

        if choix == "1":
            if endurance >= 10:
                deg = random.randint(20, 35) + rage // 10
                endurance -= 10
                boss_vie -= deg
                print(f"⚔️ Dragonslayer tranche la chair : -{deg}")
            else:
                lent("❌ Trop fatigué.")

        elif choix == "2":
            if endurance >= 20:
                deg = random.randint(35, 55)
                endurance -= 20
                boss_vie -= deg
                print(f"💥 Canon du bras explose l'ennemi : -{deg}")
            else:
                lent("❌ Pas assez d'endurance.")
        
        elif choix == "3":
            print("🩸 GUTS SE LAISSE CONSULMER PAR LA RAGE")
            rage += 25
            endurance -= 15
            deg = random.randint(25, 40)
            boss_vie -= deg
            lent(f"🔥 Massacre furieux : -{deg}")

        elif choix == "4":
            print("🛡️ Tu encaisses, dents serrées.")
            endurance += 15
            endurance  = min(100, endurance)

        else:
            lent("❌ Mauvais choix.")
            continue

        # ===== RISPOSTE =====

        if boss_vie > 0:
            dmg = random.randint(*boss["force"])
            horreur = boss["horreur"]

            if random.randint(1, 100) < 20:
                lent("😱 Vision infernale.")
                rage += horreur

            vie -= dmg
            lent(f"👹 L'appôtre frappe : -{dmg}")

        pause()

    # ===== FIN DE COMBAT =====

    if vie > 0:
        lent("🩸 L'apôtre tombe.")
        lent("Mais la nuit continue.")
        endurance += 20
        rage += 10
        tour += 1
        pause()

# ===== FIN =====

clair()
if vie <= 0:
    lent("💀 Ton corps s'effondre.")
    lent("Mais ta haine survit.")
else:
    lent("🏆 Tu as survécu aux damnés.")
    lent("Pour cette nuit...")

lent("\n🩸 Fin - BERSERK")