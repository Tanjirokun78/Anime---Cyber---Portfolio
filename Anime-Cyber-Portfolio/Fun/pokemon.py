import random
import time

# ====== OUTILS ======

def pause():
    input("\n⏎ Continuer...")

def lent(txt, t=0.03):
    for c in txt:
        print(c, end="", flush=True)
        time.sleep(t)
    print()

def barre(valeur, maxv=100, size=20):
    ratio = valeur / maxv
    rempli = int(ratio * size)

    if ratio < 0.3:
        symbole = "░"
    elif ratio < 0.6:
        symbole = "▒"
    elif ratio < 0.9:
        symbole = "▓"
    else:
        symbole = "█"

    return "[" + symbole * rempli + "-" * (size - rempli) + "]"

def barre_stats(valeur, max_val, icone):
    return f"{icone} {barre(valeur, max_val)} {valeur}/{max_val}"

def afficher_pokemons():
    print("\n📦 TES POKÉMONS")
    print("="*40)

    for i, p in enumerate(equipe, 1):
        print(f"\n{i}. {p['nom']}")
        print(barre_stats(p["pv"], p["pv_max"], "♥️"))
        print(f"⭐️ Niveau :{p['niveau']} | XP : {p['xp']}")

    print("="*40)
    pause()

# ====== POKÉMON SAUVAGES ======

pokemon_sauvages = {
    "Rattata": {"pv": 30, "atk": (5, 8), "taux_capture": 60},
    "Pikachu": {"pv": 45, "atk": (8, 12), "taux_capture": 40},
    "Machop": {"pv": 60, "atk": (10, 14), "taux_capture": 30},
    "Dratini": {"pv": 80, "atk": (14, 18), "taux_capture": 15},
}

# ====== TON POKÉMON (UNE SEULE SOURCE) ======

equipe = [
    {
        "nom": "Salamèche",
        "pv": 60,
        "pv_max": 60,
        "atk": (10, 25),
        "niveau": 5,
        "xp": 0
    }
]

pokemon = equipe[0]

# ====== CHASSE ======

def chasse_pokemon():
    lent("🌿 Tu explores les hautes herbes...")
    pause()

    if random.randint(1, 100) <= 70:
        nom = random.choice(list(pokemon_sauvages.keys()))
        sauvage = pokemon_sauvages[nom].copy()
        sauvage["nom"] = nom
        print(f"⚡ Un {nom} sauvage apparaît !")
        return sauvage
    else:
        print("😕 Aucun Pokémon trouvé.")
        return None

# ====== COMBAT ======

def combat(pokemon, sauvage):
    print("\n⚔️ Combat engagé !")

    while pokemon["pv"] > 0 and sauvage["pv"] > 0:

        print("\n" + "-"*40)
        print(barre_stats(pokemon["pv"], pokemon["pv_max"], "🐲"))
        print(barre_stats(sauvage["pv"], pokemon_sauvages[sauvage["nom"]]["pv"], "👾"))
        print("-"*40)

        print("""
[1] Attaquer
[2] Lancer une Pokéball
[3] Fuir
""")

        choix = input("➡ ").strip()

        # ===== ATTAQUE =====
        if choix == "1":
            degats = random.randint(*pokemon["atk"])
            sauvage["pv"] -= degats
            print(f"🔥 Tu infliges {degats} dégâts !")

        # ===== CAPTURE =====
        elif choix == "2":
            base = pokemon_sauvages[sauvage["nom"]]["taux_capture"]
            bonus = int((1 - sauvage["pv"] / pokemon_sauvages[sauvage["nom"]]["pv"]) * 40)

            if random.randint(1, 100) <= base + bonus:
                print(f"🎉 {sauvage['nom']} est capturé !")
                return "capture"
            else:
                print("💥 Il résiste !")

        # ===== FUITE =====
        elif choix == "3":
            print("💨 Tu prends la fuite.")
            return "fuite"

        else:
            print("❌ Choix invalide.")
            continue

        # ===== RIPOSTE =====
        if sauvage["pv"] > 0:
            degats = random.randint(*sauvage["atk"])
            pokemon["pv"] -= degats
            print(f"👾 {sauvage['nom']} attaque : -{degats} PV")

        # 🔧 sécurité PV
        pokemon["pv"] = max(0, min(pokemon["pv"], pokemon["pv_max"]))

    if pokemon["pv"] <= 0:
        print("💀 Ton Pokémon est K.O.")
        return "defaite"

    print(f"✨ {sauvage['nom']} est vaincu !")
    pokemon["xp"] += 20
    return "victoire"

# ====== INTRO ======

print("""
=====================================
🐾 POKÉMON – CHASSE & COMBAT
=====================================
Ton aventure commence...
""")

pause()

# ====== BOUCLE JEU ======

jour = 1
MAX_JOURS = 10

while pokemon["pv"] > 0 and jour <= MAX_JOURS:

    print("\n" + "="*45)
    print(f"📅 JOUR {jour}")
    print(barre_stats(pokemon["pv"], pokemon["pv_max"], "❤️"))
    print(f"⭐ Niveau : {pokemon['niveau']} | XP : {pokemon['xp']}")
    print("="*45)

    print("""
Actions :
[1] Explorer les hautes herbes
[2] Centre Pokémon
[3] Quitter l'aventure
[4] Voir mes Pokemons
""")

    choix = input("➡ ").strip()

    if choix == "1":
        sauvage = chasse_pokemon()
        if sauvage:
            combat(pokemon, sauvage)

    elif choix == "2":
        print("🏥 Centre Pokémon...")
        equipe["pv"] = equipe["pv_max"]
        print("✨ Ton Pokémon est soigné.")

    elif choix == "3":
        print("👋 Tu ranges tes Pokéballs.")
        break
    
    elif choix == "4":
        afficher_pokemons()
    
    # ===== ÉVÉNEMENT RARE =====
    if random.randint(1, 1000) <= 5:
        lent("\n🌌 Une présence légendaire...")
        lent("Un Pokémon légendaire apparaît.")
        lent("Tu n'étais pas prêt.")
        equipe["pv"] = 0
        break

    jour += 1
    pause()

# ====== FIN ======

print("\n" + "="*45)

if pokemon["pv"] <= 0:
    lent("💀 Ton aventure s'arrête ici...")

else:
    lent("🏆 Tu survis à cette aventure Pokémon.")

print("\nMerci d'avoir joué 🐾")
