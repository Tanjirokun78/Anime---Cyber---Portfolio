import random

print("📓 DEATH NOTE - Jeu de Déduction\n")

role = random.choice(["Kira", "L"])
suspicion = 0
opposants = 3
tour = 1

print("Le jeu commence...")
print("Ton rôle est caché.\n")

while tour <= 5:
	print(f"\n🔁 Tour {tour}")

	if role == "Kira":
		print("1. Éliminer discrètement ")
		print("2. Ne rien faire")
		choix = input("➡ Ton choix : ")

		if choix == "1":
			opposants -= 1
			suspicion += random.randint(15,30)
			print("☠️ Un  opposant est éliminé.")
		else:
			suspicion -= 5
			print("😶 Tu restes discret. ")

		print(f"👁 Suspicion : {suspicion}%")
	
		if  suspicion >= 100:
			print("\n⚖️ Tu as été découvert.")
			print("❌ Défaite de Kira.")
			break

		if opposants == 0:
			print("\n👑 Tous tes opposants sont éliminés.")
			print("✅ Victoire de Kira.")
			break
	
	else: #L
		print("1. Observer")
		print("2. Interroger")
		print("3. Accuser")
		choix = input("➡Ton Choix : ")
		
		chance = random.randint(1, 100)

		if choix == "3":
			if chance > 65:
				print("\n⚖️ Kira est identifié.")
				print("✅ Victoire de L.")
				break
		else:
			print("🔍 Tu collectes des informations...")
			if chance > 75:
				print("💡 Tu te rapproches de la vérité.")

	tour += 1

if tour > 5:
	print("\n⌛️ Le temps est écoulé.")
	print("La vérité reste inconnue...")
