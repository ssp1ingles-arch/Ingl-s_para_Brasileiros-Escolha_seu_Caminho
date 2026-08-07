@echo off
REM ============================================================
REM  auto_push.bat — Push automatico do projeto
REM  Atualizado: agora sincroniza TODO o projeto Claude Code
REM  incluindo a pasta "Inglês para Brasileiros - Escolha seu Caminho"
REM ============================================================

cd "C:\Users\Samukk99\Documents\Claude Code Projetos"

echo Adicionando todos os arquivos...
git add .

echo Fazendo commit...
git commit -m "Atualizacao automatica — %date% %time%"

echo Enviando para o repositorio remoto...
git push origin main

echo.
echo ------------------------------------
echo  Push concluido com sucesso!
echo  Pasta sincronizada:
echo  Claude Code Projetos (completo)
echo    - Americano_01
echo    - Sala_001
echo    - Ingles para Brasileiros - Escolha seu Caminho
echo       Sistema 01 - Base. Fluencia. Gramatica
echo       Sistema 02 - Reducoes do Ingles Real
echo       Sistema 03 - Motor de Verbos
echo       Sistema 04 - Conectar Frases
echo       Sistema 05 - Situar a Frase
echo       Sistema 06 - Definir nome
echo ------------------------------------
pause