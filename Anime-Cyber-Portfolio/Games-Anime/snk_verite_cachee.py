import random

# ========= OUTILS =========

def pause():
    input("\n⏎ Appuie sur Entrée pour continuer...")

def barre(valeur, max_val=100, taille=20):
    rempli = int((valeur / max_val) * taille)
    return "[" + "#" * rempli + "-" * (taille - rempli) + "]"

# ========= INTRO =========

print("""
========================================
     🧱 SHINGEKI NO KYOJIN
        VÉRITÉ CACHÉE
========================================
Un Titan se cache parmi eux 🎭.
Observe. Analyse. Accuse.
""")
pause()

# ========= PERSONNAGES =========

personnages = {
    "Eren": {"suspicion": random.randint(10, 30)},
    "Reiner": {"suspicion": random.randint(10, 30)},
    "Annie": {"suspicion": random.randint(10, 30)},
    "Armin": {"suspicion": random.randint(10, 30)}
}

titan_cache = random.choice(list(personnages.keys()))

verite = 0
tour = 1
MAX_TOURS = 6

# ========= BOUCLE PRINCIPALE =========

while tour <= MAX_TOURS:
    print(f"\n🕒 TOUR {tour}")
    print("État des soupçons :\n")

    for nom, data in personnages.items():
        print(f"- {nom} : {barre(data['suspicion'])} {data['suspicion']}%")

    print("\nQue fais-tu ?")
    print("[1] Observer un comportement")
    print("[2] Interroger quelqu'un")
    print("[3] Ne rien faire")

    choix = input("➡ Ton choix : ").strip()

    if choix == "1":
        cible = random.choice(list(personnages.keys()))
        gain = random.randint(5, 15)
        personnages[cible]["suspicion"] += gain 
        verite += 5
        print(f"👁️ Tu observes {cible} (+{gain}% suspicion).")

    elif choix == "2":
        cible =random.choice(list(personnages.keys()))
        gain = random.randint(-5, 20)
        personnages[cible]["suspicion"] += gain
        verite += 10
        print(f"🗣️ Interrogatoire de {cible} (variation {gain}%).")
    
    else:
        print("😶 Tu restes silencieux.")
        verite += 2

    #Clamp valeurs
    for p in personnages:
        personnages[p]["suspicion"] = max(0, min(100, personnages[p]["suspicion"]))

    print("\n🔎 Progression vers la vérité :", barre(verite), f"{verite}%")

    pause()
    tour += 1

# ========= ACCUSATION FINALE =========

print("\n⚖️ ACCUSATION FINALE")
print("Tu n'as plus le temps.")
print("Qui est le Titan selon toi ?\n")

for p in personnages:
    print("-", p)

choix = input("\n➡ Nom du Titan : ").strip()

print("\n⏳ Verdict...\n")

if choix == titan_cache:
    print("🎯 ACCUSATION CORRECTE")
    print(f"{titan_cache} était bien le Titan.")
    print("🕊️ L'humanité survit.")
else:
    print("❌ MAUVAISE ACCUSATION")
    print(f"Le vrai Titan était : {titan_cache}")
    print("🔥 L'humanité est condamnée.")

print("\n--- FIN ---")