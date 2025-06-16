import os
import time
import psutil
from datetime import datetime
import subprocess

# Caminhos dos bots
bots = {
    "main.py": r"C:\Users\Dinis Narciso\nowplaying-bot\main.py",
    "spotify.py": r"C:\Users\Dinis Narciso\spotify-bot\main.py"
}

log_file = os.path.join(os.path.dirname(__file__), "watchdog.log")

def log(mensagem):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} {mensagem}\n")

def processo_em_execucao(script):
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if 'python.exe' in proc.info['name'].lower() and script in ' '.join(proc.info['cmdline']):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False

log("Watchdog iniciado. Verificacoes a cada 2 minutos.")

while True:
    for nome, caminho in bots.items():
        if not processo_em_execucao(nome):
            subprocess.Popen(["python", caminho], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            log(f"Reiniciado: {caminho}")
        else:
            log(f"Ja em execucao: {caminho}")
    log("Verificacao concluida.")
    time.sleep(120)