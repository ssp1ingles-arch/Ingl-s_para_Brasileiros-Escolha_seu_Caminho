@echo off
REM ============================================================
REM  auto_push.bat — Push automatico do projeto
REM  Local: Ingles para Brasileiros - Escolha seu Caminho
REM  A raiz do repositorio git agora e ESTA pasta (onde fica
REM  o index.html), para o GitHub Pages servir a partir da raiz.
REM ============================================================

REM /d garante troca de unidade caso necessario.
cd /d "C:\Users\Samukk99\Documents\Claude Code Projetos\Inglês para Brasileiros - Escolha seu Caminho"

echo Pasta atual do git:
cd
echo.

echo Adicionando todos os arquivos...
git add .

echo Fazendo commit...
git commit -m "Atualizacao automatica — %date% %time%"

echo Enviando para o repositorio remoto...
git push origin main

echo.
echo ------------------------------------
echo  Push concluido com sucesso!
echo  Raiz do repositorio (com index.html):
echo  Ingles para Brasileiros - Escolha seu Caminho
echo    - index.html  (painel principal / GitHub Pages)
echo    - sistemas.json
echo    - Sistema 01 ... Sistema 09
echo ------------------------------------
pause
