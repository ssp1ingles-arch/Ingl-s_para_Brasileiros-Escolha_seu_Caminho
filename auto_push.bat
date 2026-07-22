@echo off
chcp 65001 >nul
REM ============================================================
REM  auto_push.bat — Push automatico do projeto
REM  Local: Ingles para Brasileiros - Escolha seu Caminho
REM  A raiz do repositorio git e ESTA pasta (onde fica o
REM  index.html), para o GitHub Pages servir a partir da raiz.
REM
REM  IMPORTANTE: usamos %~dp0 (a pasta DESTE .bat) em vez de um
REM  caminho fixo. O caminho tem acentos (Ingles/Caminho) e, se
REM  fixo no arquivo, o cmd falha com "O sistema nao pode
REM  encontrar o caminho especificado" por causa da codepage.
REM  %~dp0 resolve a pasta correta em qualquer situacao.
REM ============================================================

REM /d garante troca de unidade caso necessario.
cd /d "%~dp0"

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
echo    - index.html   (painel principal / GitHub Pages)
echo    - sistemas.json
echo    - Sistema 01 ... Sistema 07
echo    - Sistema 08 — Baseado em Livros (V01 a V06 — Kids)
echo    - Sistema 09 — Duvidas Pontuais
echo    - Sistema 10 — Pratica Completa · 4 Pilares
echo ------------------------------------
pause
