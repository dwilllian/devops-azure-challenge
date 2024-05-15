
import json
import psutil
import subprocess
import os

def uso_cpu():
    return psutil.cpu_percent(interval=1)

def uso_memoria():
    memoria = psutil.virtual_memory()
    return {
        'total': memoria.total,
        'disponivel': memoria.available,
        'percentual': memoria.percent,
        'usada': memoria.used,
        'livre': memoria.free
    }

def uso_disco():
    disco = psutil.disk_usage('/')
    return {
        'total': disco.total,
        'usado': disco.used,
        'livre': disco.free,
        'percentual': disco.percent
    }

def atualizacoes_pendentes():
    try:
        resultado = subprocess.run(['apt', 'list', '--upgradable'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        atualizacoes = resultado.stdout.split('\n')[1:-1]
        return {'atualizacoes': len(atualizacoes)}
    except Exception as e:
        return {'erro': str(e)}

def estatisticas_dstat():
    try:
        resultado = subprocess.run(['dstat', '--json'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        estatisticas = json.loads(resultado.stdout)
        return estatisticas
    except Exception as e:
        return {'erro': str(e)}

def estatisticas_sistema():
    estatisticas = {
        'uso_cpu': uso_cpu(),
        'uso_memoria': uso_memoria(),
        'uso_disco': uso_disco(),
        'atualizacoes_pendentes': atualizacoes_pendentes(),
        'estatisticas_dstat': estatisticas_dstat()
    }
    return json.dumps(estatisticas, indent=4)

if __name__ == "__main__":
    if os.system("which dstat") != 0:
        print("Dstat não está instalado. tentando instalar...")
        os.system("sudo apt-get update && sudo apt-get install -y dstat")
    print(estatisticas_sistema())
