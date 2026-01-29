"""
Este programa es creado para organizar los documentos 
por tipo en cualquier carpeta solo dando la ruta de la carpeta.
Desarrollado por Omarmp25
"""

import os
import shutil
import time
import sys

def limpiar_pantalla():
    # Limpia la terminal dependiendo del sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

# 1. Menú de bienvenida
limpiar_pantalla()

# Definición de colores ANSI
VERDE = "\033[0;32m"
CIAN  = "\033[0;36m"
AMARILLO = "\033[0;33m"
GRIS = "\033[0;90m"
RESET = "\033[0m"

def imprimir_bienvenida_zen():
    # El dibujo del Buda en formato Raw para evitar errores de escape | creditos a: https://www.asciiart.eu/religion/buddha
    buda_ascii = rf"""
{CIAN}            || Organizador de documentos|| {RESET}
{VERDE}
                           _
                        _ooOoo_
                       o8888888o
                       88" . "88
                       (| -_- |)
                       O\  =  /O
                    ____/`---'\____
                  .'  \\|     |//  `.
                 /  \\|||  :  |||//  \
                /  _||||| -:- |||||_  \
                |   | \\\  -  /'| |   |
                | \_|  `\`---'//  |_/ |
                \  .-\__ `-. -'__/-.  /
              ___`. .'  /--.--\  `. .'___
           ."" '<  `.___\_<|>_/___.' _> \"".
          | | :  `- \`. ;`. _/; .'/ /  .' ; |
          \  \ `-.   \_\_`. _.'_/_/  -' _.' /
===========`-.`___`-.__\ \___  /__.-'_.'_.-'===========
                        `=--=-'
{RESET}
           {AMARILLO}"Mente clara, Escritorio tambien"{RESET}
    """
    print(buda_ascii)

# Ejecución
imprimir_bienvenida_zen()
print(f"{CIAN}Esperando la ruta...{RESET}")

print("\tEjemplo: C:/Users/TuUsuario/Downloads")

# 2. Entrada de ruta manual
ruta_objetivo = input("\n📂 Pega la ruta de la carpeta: ").strip()

# Limpieza de comillas por si se copia la ruta con ellas
ruta_objetivo = ruta_objetivo.replace('"', '').replace("'", "")

# 3. Diccionario de organización (Categorías)
formatos = {
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".html", ".pbix"],
    "Hojas de calculo": [".xls", ".xlsx", ".csv"],
    "Presentaciones": [".ppt", ".pptx"],
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".ico"],
    "Ejecutables": [".exe", ".msi"],
    "Comprimidos": [".zip", ".rar", ".7z"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Libros": [".epub", ".mobi", ".azw3"],
    "Codigo_Programacion": [".py", ".ipynb", ".js", ".html", ".css"], 
    "Audio": [".mp3", ".wav", ".m4a"]
}

# 4. Verificación y Proceso
if os.path.exists(ruta_objetivo):
    # --- ANIMACIÓN DEL COHETE --- 
    limpiar_pantalla()
  # --- ANIMACIÓN DE CARGA NEUTRA (5 SEGUNDOS) ---
    print(f"\n{CIAN}🛠️  Preparando carpeta: {ruta_objetivo}{RESET}")
    print(GRIS + "-------------------------------------------------------" + RESET)
    
    # 25 pasos para completar los 5 segundos (0.2s cada uno)
    for i in range(25):
        # Un símbolo de carga discreto
        simbolo = "🔸" if i % 2 == 0 else "🔹"
        print(simbolo, end="", flush=True)
        time.sleep(0.2)
        
    print(f" {VERDE}✅ Archivos organizados. ¡Excelente día!{RESET}")
    print(GRIS + "-------------------------------------------------------" + RESET + "\n")
    # --- FIN DE LA ANIMACIÓN ---

    archivos = os.listdir(ruta_objetivo)
    contador = 0

    for archivo in archivos:
        # Solo procesamos archivos, no carpetas
        ruta_completa_archivo = os.path.join(ruta_objetivo, archivo)
        
        if os.path.isfile(ruta_completa_archivo):
            nombre, ext = os.path.splitext(archivo)
            ext = ext.lower()
            
            for carpeta, extensiones in formatos.items():
                if ext in extensiones:
                    ruta_destino = os.path.join(ruta_objetivo, carpeta)
                    
                    # Crear la carpeta de categoría si no existe
                    os.makedirs(ruta_destino, exist_ok=True)
                    
                    # Mover el archivo al nuevo destino
                    shutil.move(ruta_completa_archivo, os.path.join(ruta_destino, archivo))
                    print(f"✅ {archivo} movido a -> {carpeta}")
                    contador += 1
    
    print(f"\n\t | ✨ ¡Listo! Se organizaron {contador} archivos. ✨ |\n")
else:
    print("\n❌ Esa ruta no existe. Por Favor, revisa que esté bien escrita.\n")
    
input("Presiona Enter para salir...")       
