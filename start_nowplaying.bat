@echo off
echo Iniciando servidor Replit local...
start cmd /k "cd /d C:\Users\Dinis Narciso\nowplaying-bot && python main.py"

timeout /t 2 /nobreak >nul

echo Iniciando o atualizador do Spotify...
start cmd /k "cd /d C:\Users\Dinis Narciso\spotify-bot && python main.py"
