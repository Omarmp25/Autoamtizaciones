@echo off
:: 1. Entramos a la carpeta real del proyecto
cd /d "C:\Users\halo_\OneDrive\Desktop\VS Code proyectos\Autoamtizaciones"

:: 2. Activamos tu entorno virtual
call ".\env\Scripts\activate"

:: 3. Ejecutamos el script desde la ubicación actual
py "Organizador_de_carpetas.py"

pause