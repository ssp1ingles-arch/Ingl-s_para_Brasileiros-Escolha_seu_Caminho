@echo off
chcp 65001 > nul
cd /d "%~dp0"
echo Pasta atual do git:
cd
echo.
echo Adicionando arquivos...
git add .
echo Fazendo commit...
git commit -m "Atualizacao automatica"
echo Enviando para o repositorio remoto...
git push origin main
echo.
echo ------------------------------------
echo  Push concluido!
echo ------------------------------------
pause
