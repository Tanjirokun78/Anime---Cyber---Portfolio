def analyser_logs(fichier):
	demons_detectes = {
		"WARNING": "Démon de la Latence",
		"ERROR": "Démon du Timeout",
		"CRITICAL": "Démon de la Sécurité"
	}
	
	compteur = {
		"WARNING": 0,
		"ERROR": 0,
		"CRITICAL": 0
	}

	print("🪚 Analyse des logs en cours...\n")
	
	with open(fichier, "r") as f:
		for ligne in f:
			for niveau in demons_detectes:
				if niveau in ligne:
					compteur[niveau] += 1
					print(f"⚠️ {demons_detectes[niveau]} détecté → {ligne.strip()}")
	
	print("\n📊 Rapport final")
	for niveau, nombre in compteur.items():
		print(f"{demons_detectes[niveau]} : {nombre}")

analyser_logs("logs.txt")

print("\nExplications 😊 : Les logs sont le monde réel. ")
print("\nLes démons sont les problèmes cachés.")
print("\nMon script, c’est le chasseur.")
