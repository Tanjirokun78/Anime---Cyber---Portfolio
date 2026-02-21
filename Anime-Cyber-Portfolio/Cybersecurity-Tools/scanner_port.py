import socket
import time

# ====== INTRO ======
print("🔒 Mini Scanner de Ports - Test de sécurité")
print("⚠️ Scanne uniquement tes machines ou autorisées !\n")
time.sleep(1)

# ====== INPUT ======
target = input("➡ IP ou hostname à scanner : ").strip()
start_port = int(input("Port de départ : "))
end_port = int(input("Port de la fin : "))

print(f"\n⏳ Scan de {target} de {start_port} à {end_port}...\n")
time.sleep(1)

# ====== SCAN ======
for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)    # temps max pour chaque port
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"✅ Port {port} ouvert")
    else:
        print(f"❌ Port {port} fermé")
    sock.close()

print("\n🎯 Scan terminé !")