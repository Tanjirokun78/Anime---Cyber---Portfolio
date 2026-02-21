import random
import time

# ====== OUTILS =====

def pause():
    input("\n⏎ Continuer...")

def lent(txt, t=0.03):
    for c in txt:
        print(c , end="", flush=True)
        time.sleep(t)
    print()
    
def barre(valeur, maxv=8000, size=25):
    ratio = valeur / maxv
    rempli = int(ratio * size)
    return "[" + "█" * rempli + "-" * (size - rempli) + "]"

def piocher_carte():
    if not deck:
        return None
    carte = random.choice(deck)
    deck.remove(carte)
    main.append(carte)
    return carte

def afficher_cimetiere():
    print("\n🪦 CIMETIÈRE")
    print("="*30)
    if not cimetiere:
        print("Vide.")
    else:
        for carte in cimetiere:
            print(f"- {carte['nom']}")

def tenter_fusion():
    lent("\n🔮 Tentative de Fusion...")

    for nom_fusion, data in fusions.items():
        requis = data["necessaire"].copy()
        cartes_dispo = [c["nom"] for c in deck + cimetiere]

        possible = True
        for carte in requis:
            if carte in cartes_dispo:
                cartes_dispo.remove(carte)
            else:
                possible = False
                break
        
        if possible:
            lent(f"✨ FUSION RÉUSSIE : {nom_fusion} !")

            # retirer les cartes utilisées
            for carte_nom in requis:
                for zone in (deck, cimetiere):
                    for c in zone:
                        if c["nom"] == carte_nom:
                            zone.remove(c)
                            break

            return data["puissance"]

    lent("❌ Aucune fusion possible.")
    return None 

def invoquer_dieu():
    lent("\n🔱 Invocation d'un Dieu Égyptien...")

    print("\nDieu disponibles :")
    for i, nom in enumerate(dieux_egyptiens.keys(), 1):
        print(f"{i} {nom}")
    
    choix = input("➡ Choisis un Dieu : ").strip()
    noms = list(dieux_egyptiens.keys())

    if not choix.isdigit() or int(choix) not in range(1, len(noms)+1):
        lent("❌ Choix invalide.")
        return None 
    
    dieu = noms[int(choix)-1]
    data = dieux_egyptiens[dieu]

    if len(main) < data["sacrifices"]:
        lent("❌ Pas assez de sacrifices.")
        return None

    # sacrifices
    for _ in range(data["sacrifices"]):
        carte = main.pop(0)
        cimetiere.append(carte)
    
    lent(f"✨ {dieu} est invoqué !")

    return dieu, data

def afficher_main():
    print("\n🤚 TA MAIN")
    print("=" * 30)
    if not main:
        print("Main vide.")
    else:
        for i, carte in enumerate(main, 1):
            print(f"[({i})] {carte['nom']} ({carte['type']})")

cartes_disponibles = [
    {"nom": "Dragon Blanc aux Yeux Bleus", "type": "attaque", "puissance": 3000},
    {"nom": "Magicien Sombre", "type": "attaque", "puissance": 2500},
    {"nom": "Dragon Noir aux Yeux Rouges", "type": "attaque", "puissance": 2400},
    {"nom": "Kuriboh", "type": "defense", "reduction": 1000},
    {"nom": "Force Miroir", "type": "piege", "effet": "contre"},
    {"nom": "Foudre Noire", "type": "magie", "effet": "degâts"},
    {"nom": "Pot de Cupidité", "type": "magie", "effet": "pioche"},
    {"nom": "Terrain Feu", "type": "terrain", "terrain": "Feu"},
    {"nom": "Terrain Ténèbres", "type": "terrain", "terrain": "Ténèbres"},
    {"nom": "Terrain Lumière", "type": "terrain", "terrain": "Lumière"},
    
    
]
fusions = {
    "Dragon Ultime": {
        "necessaire": [
            "Dragon Blanc aux Yeux Bleus",
            "Dragon Blanc aux Yeux Bleus",
            "Dragon Blanc aux Yeux Bleus"
        ],
        "puissance" : 4500
    }
}
# ====== DIEUX ÉGYPTIENS ======
dieux_egyptiens = {
    "Obelisk le Tourmenteur": {
        "sacrifices": 3,
        "degats": 4000
    },
    "Slifer le Dragon Céleste": {
        "sacrifices": 3,
        "degats": 3500
    },
    "Le Dragon Ailé de Râ": {
        "sacrifices": 3,
        "degats": "ALL"
    }
}
# ====== TERRAINS ======
terrains = {
    "Neutre": {
        "attaque": 1.0,
        "magie": 1.0
    },
    "Feu": {
        "attaque": 1.2,
        "magie": 0.9
    },
    "Ténèbres" : {
        "attaque": 1.1,
        "magie": 1.1
    },
    "Lumière": {
        "attaque": 0.9,
        "magie": 1.2
    }
}
def contruire_deck():
    deck = []
    MAX_CARTES = 5

    lent("🃏 BIENVENUE DANS LE DECKBUILDER.")
    lent(f"Choisis {MAX_CARTES} cartes pour ton deck.\n")

    while len(deck) < MAX_CARTES:
        print("\nCartes disponibles :")
        for i, carte in enumerate(cartes_disponibles, 1):
            print(f"[{i}] {carte['nom']} ({carte['type']})")

        choix = input("➡ Numéro de la carte : ").strip()

        if not choix.isdigit():
                print("❌ Choix invalide.")
                continue

        choix = int(choix)

        if 1 <= choix <= len(cartes_disponibles):
            carte = cartes_disponibles[choix - 1]
            deck.append(carte)
            print(f"✅ {carte['nom']} ajoutée au deck.")
            print(f"📦 Deck : {len(deck)}/{MAX_CARTES}")
        else:
            print("❌ Numéro incorrect.")

    lent('\n🔥 Deck terminé !')
    return deck

# ====== CRÉATION DU DECK ======

deck = contruire_deck()
main = []
# ====== CIMETIÈRE ======
cimetiere = []
# ====== TERRAIN ======
terrain_actuel = "Neutre"
# ====== MAIN DE DÉPART ======
for _ in range(3):
    if deck:
        carte = random.choice(deck)
        deck.remove(carte)
        main.append(carte)

pause()

# ====== INTRO ======
print("========================================")
print("🃏 YU-GI-OH – DUEL DES OMBRES")
print("========================================")
lent("🌌 La nuit tombe sur l'arène...")
lent("Un duel se prépare.")
lent("Les cartes décident du destin.")
pause()

# ====== JOUEUR ======

joueur = {
    "nom": "Dueliste",
    "pv": 8000,
    "energie": 100,
}

adversaires = [
    {"nom": "Seto Kaiba", "pv": 8000, "style": "agressif"},
    {"nom": "Marik", "pv": 7000, "style": "ombre"},
    {"nom": "Pegasus", "pv": 6000, "style": "piège"}
]

ennemi = random.choice(adversaires)

# ====== DUEL ======

lent(f"🔥 {ennemi['nom']} apparaît !")
pause()

tour = 1

while joueur["pv"] > 0 and ennemi["pv"] > 0 and (deck or main):

    print("\n" + "="*45)
    print(f"🔁 TOUR {tour}")
    if deck:
        piocher_carte()
        lent("📥 Tu pioches une carte.")
    print(f"🧍‍♂️ {joueur['nom']} {barre(joueur['pv'])} {joueur['pv']} LP")
    print(f"👹 {ennemi['nom']} {barre(ennemi['pv'])} {ennemi['pv']} LP")
    print(f"🌍 Terrain : {terrain_actuel}")
    print(f"🃏 Deck : {len(deck)} | Main : {len(main)}")
    print("="*45)

    print("""
Actions :
[1] Attaquer
[2] Jouer une carte de la main
[3] Poser un piège
[4] Fusion
[5] Invoquer un Dieu Égyptien
[6] Finir le tour 
[7] Voir le cimetière
""")
    
    choix = input("➡ ").strip()

    # ====== ATTAQUE ======
    if choix == "1":
        degats = random.randint(500, 1500)
        ennemi["pv"] -= degats
        lent(f"⚔️  Attaque directe ! -{degats} LP")

    # ====== MAGIE ======
    elif choix == "2":
        afficher_main()
        if not carte:
            lent("❌ tu n'as plus aucune carte en main.")
        else:
            choix_carte = input("➡ Numéro de la carte à jouer : ").strip()

            if not choix_carte.isdigit():
                lent("❌ Choix invalide.")
            else:
                choix_carte = int(choix_carte)  
                if 1 <= choix_carte <= len(main):
                    carte = main.pop(choix_carte - 1)
                    lent(f"🃏 Tu joues : {carte['nom']}")

                    if carte["type"] == "attaque":
                        bonus = terrains[terrain_actuel]["attaque"]
                        degats = int(carte["puissance"] * bonus)
                        ennemi["pv"] -= degats
                        lent(f"💥 Bonus terrain x{bonus} → -{degats} LP")
            
                    elif carte["type"] == "magie":
                        if carte["effet"] == "degats":
                            bonus = terrains[terrain_actuel]["magie"]
                            degats = int(1500 * bonus)
                            ennemi["pv"] -= degats
                            lent(f"🔥 Magie amplifiée x{bonus} →  -{degats} LP")
                        elif carte["effet"] == "pioche":
                            for _ in range(2):
                                if deck:
                                    piocher_carte()
                            lent("📜 Tu pioches 2 cartes !")
                        
                        elif carte["type"] == "terrain":
                            terrain_actuel = carte["terrain"]
                            lent(f"🌍 Le terrain devient : {terrain_actuel} !")

                    elif carte["type"] == "defense":
                        joueur["pv"] += carte["reduction"]
                        lent(f"🛡️ +{carte['reduction']} LP")
            
                    cimetiere.append(carte)
                    lent("🪦 Carte envoyée au cimetière")
                else:
                    lent("❌ Numéro incorrect.")

    # ====== PIÈGE ======
    elif choix == "3":
        lent("🪤 Tu poses un piège")
        if random.randint(1, 100) < 40:
            ennemi["pv"] -= 1500
            lent("💥 Piège activé ! -1500 LP")
        else:
            lent("😬 Le piège s'active pas...")

    # ====== FUSION ======
    elif choix == "4":
        puissance = tenter_fusion()
        if puissance:
            ennemi["pv"] -= puissance
            lent(f"💥 ATTAQUE DE FUSION ! -{puissance} LP")
    
    # ====== DIEUX ÉGYPTIENS ======
    elif choix == "5":
        resultat = invoquer_dieu()
        if resultat:
            dieu, data = resultat

            if data["degats"] == "ALL":
                lent("🔥 RÂ SACRIFICE TA VIE !")
                ennemi["pv"] = 0
                joueur["pv"] = 1
            else:
                ennemi["pv"] -= data["degats"]
                lent(f"💥 {dieu} attaque ! -{data['degats']} LP")


    # ====== FIN TOUR ======
    elif choix == "6":
        lent("🔚 Tu termines ton tour.")


    # ====== VOIR CIMETIÈRE ======
    elif choix == "7":
        afficher_cimetiere()
    else:
        lent("❌ Action invalide.")   

    # ====== RISPOSTE ENNEMI ======
    if ennemi["pv"] > 0:
        lent("\n👹 Tour de l'adversaire...")
        time.sleep(1)

        if ennemi["style"] == "agressif":
            degats = random.randint(800, 1800)

        elif ennemi["style"] == "ombre":
            degats = random.randint(600, 1400)
            joueur["energie"] -= 10
            print(f"{ennemi} te drain -10 d'énergie...")

        else:
            degats= random.randint(500, 1200)

        joueur["pv"] -= degats
        lent(f"💥 {ennemi['nom']} attaque ! -{degats} LP")

    # ====== LIMITES ======
    joueur["pv"] = max(0, min(8000, joueur["pv"]))
    ennemi["pv"] = max(0, ennemi["pv"]) 
    joueur["energie"] = max(0, joueur["energie"])

    # ====== FIN SECRÈTE ======
    if random.randint(1, 1000) <= 5:
        lent("\n👁️ Une présence ancienne...")
        lent("EXODIA apparaît.")
        lent("Tu es anéanti instantanément.")
        joueur["pv"] = 0
        break

    tour += 1
    pause()

# ====== FIN ======

print("\n" + "="*45)

if joueur["pv"] <= 0:
    lent("☠️  Tu as perdu le Duel des Ombres...")

elif ennemi["pv"] <= 0:   
    lent("🏆 VICTOIRE !")
    lent("Ton nom résonne parmi les duellistes.")

else:
    lent("🃏 Ton deck est vide...")
    lent("La partie est terminée.")

print("\nMerci d'avoir joué :) 🃏")
