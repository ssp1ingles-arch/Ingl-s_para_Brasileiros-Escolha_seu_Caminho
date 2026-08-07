@echo off
chcp 65001 >nul
REM ============================================================
REM  organizar_sistemas.bat
REM  Copia arquivos de Americano_01 e Sala_001 para os Sistemas
REM  corretos dentro de "Inglês para Brasileiros - Escolha seu Caminho"
REM  NUNCA apaga os originais — apenas copia
REM ============================================================

set SRC=C:\Users\Samukk99\Documents\Claude Code Projetos\Americano_01
set DEST=C:\Users\Samukk99\Documents\Claude Code Projetos\Inglês para Brasileiros - Escolha seu Caminho
set S01=%DEST%\Sistema 01 — Base. Fluência. Gramática
set S02=%DEST%\Sistema 02 — Reduções do Inglês Real
set S03=%DEST%\Sistema 03 — Motor de Verbos
set S04=%DEST%\Sistema 04 — Conectar Frases
set S05=%DEST%\Sistema 05 — Situar a Frase
set S06=%DEST%\Sistema 06 — Definir nome
set ADMIN=%S01%\_admin

REM Criar pasta _admin se nao existir
if not exist "%ADMIN%" mkdir "%ADMIN%"

echo.
echo ============================================================
echo  COPIANDO ARQUIVOS ADMIN / META para _admin
echo ============================================================
copy "%SRC%\auto_push.bat" "%ADMIN%\" /Y
copy "%SRC%\HANDOFF_PAINEL_PRINCIPAL.md" "%ADMIN%\" /Y
copy "%SRC%\HANDOFF_SISTEMA28.md" "%ADMIN%\" /Y
copy "%SRC%\handoff_tecnico_ingles_brasileiros.md" "%ADMIN%\" /Y
copy "%SRC%\jornada_completa.md" "%ADMIN%\" /Y
copy "%SRC%\PROMPT_REDESIGN_PAINEL.md" "%ADMIN%\" /Y
copy "%SRC%\arquivos_processados.json" "%ADMIN%\" /Y
copy "%SRC%\sequencia_aprendizado_s1_s27.png" "%ADMIN%\" /Y

echo.
echo ============================================================
echo  SISTEMA 01 — Base. Fluência. Gramática
echo  (frases, conversas, shadowing, fluência geral)
echo ============================================================
REM sistema2: Inglês Real do Dia a Dia (frases crescentes, forma falada)
copy "%SRC%\sistema2_conteudo.md" "%S01%\" /Y
REM sistema3: Gramática Viva (12 tempos verbais) — vai também ao S03
copy "%SRC%\sistema3_conteudo.md" "%S01%\" /Y
REM sistema4: Inglês em Cena (diálogos, cenas, vocabulário)
copy "%SRC%\sistema4_conteudo.md" "%S01%\" /Y
REM sistema5: Frases Relâmpago (shadowing, 150 frases curtas)
copy "%SRC%\sistema5_conteudo.md" "%S01%\" /Y
REM sistema6: Conversas do Dia a Dia (Q&A, speak like a native)
copy "%SRC%\sistema6_conteudo.md" "%S01%\" /Y
REM sistema7: Colocações Naturais (vai também ao S06 e S03)
copy "%SRC%\sistema7_conteudo.md" "%S01%\" /Y
REM sistema9-20: CLASSIFICADOS COMO BASE (conteudo não lido individualmente — default S01)
copy "%SRC%\sistema9_conteudo.md" "%S01%\" /Y
copy "%SRC%\sistema10_conteudo.md" "%S01%\" /Y
copy "%SRC%\sistema11_conteudo.md" "%S01%\" /Y
copy "%SRC%\sistema12_conteudo.md" "%S01%\" /Y
copy "%SRC%\sistema13_conteudo.md" "%S01%\" /Y
copy "%SRC%\sistema14_conteudo.md" "%S01%\" /Y
copy "%SRC%\sistema15_conteudo.md" "%S01%\" /Y
copy "%SRC%\sistema16_conteudo.md" "%S01%\" /Y
copy "%SRC%\sistema17_conteudo.md" "%S01%\" /Y
copy "%SRC%\sistema18_conteudo.md" "%S01%\" /Y
copy "%SRC%\sistema19_conteudo.md" "%S01%\" /Y
copy "%SRC%\sistema20_conteudo.md" "%S01%\" /Y
REM sistema22: Inglês para Situações Reais (frases por situação) — vai também ao S03
copy "%SRC%\sistema22_conteudo.md" "%S01%\" /Y
REM sistema23: Inglês do Zero: Verbos, Tempos A1+A2 — vai também ao S03
copy "%SRC%\sistema23_conteudo.md" "%S01%\" /Y
REM sistema24: Pense em Inglês (estratégias de fluência)
copy "%SRC%\sistema24_conteudo.md" "%S01%\" /Y
REM sistema25: Super Sentences Vol.2 (histórias progressivas)
copy "%SRC%\sistema25_conteudo.md" "%S01%\" /Y
REM sistema26: Diálogos do Dia a Dia (conversas reais em 12 situações)
copy "%SRC%\sistema26_conteudo.md" "%S01%\" /Y
REM sistema27: Shadowing com Propósito (7 textos de mentalidade)
copy "%SRC%\sistema27_conteudo.md" "%S01%\" /Y

echo.
echo ============================================================
echo  SISTEMA 02 — Reduções do Inglês Real
echo  (contrações, forma falada, informal spoken English)
echo ============================================================
REM sistema2 contém seção "FORMA FALADA" com reduções como "aim always tired"
copy "%SRC%\sistema2_conteudo.md" "%S02%\" /Y

echo.
echo ============================================================
echo  SISTEMA 03 — Motor de Verbos
echo  (tempos verbais, verbos modais, conjugação)
echo ============================================================
REM sistema3: Gramática Viva — OS 12 TEMPOS VERBAIS
copy "%SRC%\sistema3_conteudo.md" "%S03%\" /Y
REM sistema7: Colocações Naturais — Stop Choosing Wrong Verbs
copy "%SRC%\sistema7_conteudo.md" "%S03%\" /Y
REM sistema22: Inglês para Situações Reais — phrasal verbs 50+ exemplos
copy "%SRC%\sistema22_conteudo.md" "%S03%\" /Y
REM sistema23: Inglês do Zero — Verbos, Tempos e Frases Reais A1+A2
copy "%SRC%\sistema23_conteudo.md" "%S03%\" /Y

echo.
echo ============================================================
echo  SISTEMA 04 — Conectar Frases
echo  (conectores, conjunções, linking words)
echo ============================================================
REM Nenhum arquivo específico identificado ainda — pasta criada para conteúdo futuro
echo [INFO] Sistema 04: nenhum arquivo especifico identificado nos fontes atuais.

echo.
echo ============================================================
echo  SISTEMA 05 — Situar a Frase
echo  (preposições, expressões de tempo e lugar)
echo ============================================================
REM sistema2 contém uso extensivo de preposições em contexto (at, in, on, every day etc.)
copy "%SRC%\sistema2_conteudo.md" "%S05%\" /Y
REM sistema23: menciona preposições e transporte explicitamente
copy "%SRC%\sistema23_conteudo.md" "%S05%\" /Y

echo.
echo ============================================================
echo  SISTEMA 06 — Definir nome
echo  (vocabulário, listas de palavras, definições)
echo ============================================================
REM sistema4: Inglês em Cena — vocabulário + frases-chave por cena
copy "%SRC%\sistema4_conteudo.md" "%S06%\" /Y
REM sistema7: Colocações Naturais — 100 word combinations (vocabulário)
copy "%SRC%\sistema7_conteudo.md" "%S06%\" /Y
REM sistema21: The Birthday Party — VOCABULÁRIO LITERÁRIO EM CONTEXTO
copy "%SRC%\sistema21_conteudo.md" "%S06%\" /Y
REM sistema22: Inglês para Situações Reais — phrasal verbs + idioms
copy "%SRC%\sistema22_conteudo.md" "%S06%\" /Y

echo.
echo ============================================================
echo  VERIFICANDO SALA_001...
echo ============================================================
set SRC2=C:\Users\Samukk99\Documents\Claude Code Projetos\Sala_001
if exist "%SRC2%" (
    echo Sala_001 encontrada. Copiando todos para S01 como base...
    xcopy "%SRC2%\*.*" "%S01%\Sala_001\" /E /I /Y
    echo Feito.
) else (
    echo [AVISO] Sala_001 nao encontrada em: %SRC2%
)

echo.
echo ============================================================
echo  CONCLUÍDO!
echo  Arquivos copiados. Originais preservados em:
echo  %SRC%
echo ============================================================
pauseC:\Users\Samukk99\Documents\Claude Code Projetos\Inglês para Brasileiros - Escolha seu Caminho\Sistema 01 — Base. Fluência. Gramática
