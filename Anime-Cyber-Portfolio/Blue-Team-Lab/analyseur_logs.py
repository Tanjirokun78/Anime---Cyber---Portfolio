import os

def creer_logs_si_absent(fichier):
	if not os.path.exists(fichier):
		logs = [
			"INFO Connexion réussie vers serveur-1",
			"WARNING Latence élevée détectée",
			"ERROR Timeout de connexion",
			"INFO Connexion réussie vers serveur-2",
			"Critical Accés refusé",
			"INFO Service opérationnel"
		]
		with open(fichier, "w") as f:
			for ligne in logs:
				f.write(ligne + "\n")
		print("📜 logs.txt crée automatiquement\n")

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
					print(f"⚠ {demons_detectes[niveau]} détecté  {ligne.strip()}")

	print("\n 📊 Rapport final")
	for niveau, nombre in compteur.items():
		print(f"{demons_detectes[niveau]} : {nombre}")
	
	# Niveau de danger global
	danger = (
		compteur["WARNING"] * 1 +
		compteur["ERROR"] * 2 +
		compteur["CRITICAL"] * 3
	)
	
	print("\n 🔥 Niveau de danger global :", danger)
	
	if danger == 0:
		print("🧘 Zone sécurisée")
	elif danger <= 3:
		print("⚠️ Activité  suspecte faible")
	elif danger <= 6:
		print("🚨 Menace sérieuse détectée")
	else:
		print("☠ Situation critique - intervention immédiate")

# Éxécution
fichier_logs = "logs.txt"
creer_logs_si_absent(fichier_logs)
analyser_logs(fichier_logs)
