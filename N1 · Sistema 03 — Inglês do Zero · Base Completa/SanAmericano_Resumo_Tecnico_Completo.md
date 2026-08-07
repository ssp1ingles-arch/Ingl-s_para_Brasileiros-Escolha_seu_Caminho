# SAN.AMERICANO — RESUMO TÉCNICO COMPLETO DO PROJETO
## Inglês Americano para Brasileiros | Nível A1 → A2

> **O QUE É ESTE DOCUMENTO**
> Este arquivo é um resumo técnico completo de um projeto de criação de materiais pedagógicos de inglês americano para brasileiros, desenvolvido em sessões com IA (Claude, Anthropic). Contém: histórico de decisões, evolução do projeto, metodologia, conteúdos gerados, padrão visual dos PDFs (com código-fonte completo do template), estrutura de arquivos e sugestões de continuidade. Qualquer IA ou desenvolvedor pode usar este documento para continuar o projeto exatamente de onde parou — sem que o usuário precise explicar nada novamente.

---

## 1. VISÃO GERAL DO PROJETO

**Nome do projeto:** San.Americano
**Objetivo:** Criar materiais pedagógicos de inglês americano para brasileiros de nível A1→A2, organizados em PDFs individuais temáticos, prontos para impressão ou uso digital.
**Metodologia central:** "Prompt Universal — Inglês para Brasileiros" — cada PDF cobre uma palavra ou estrutura com exemplos em afirmativo, negativo e pergunta, nos tempos presente, passado e futuro, com tradução ao português e alertas de erros comuns do brasileiro.
**Filosofia pedagógica:** Do essencial ao complementar. Do concreto ao abstrato. Estruturas fixas antes de regras abstratas. Exposição massiva a exemplos reais antes de teoria.
**Público-alvo:** Brasileiro adulto, nível A1→A2, com dificuldade em estruturas fixas, pronúncia de nativos e organização do aprendizado.

---

## 2. HISTÓRICO DE EVOLUÇÃO DO PROJETO

### Fase 1 — Verbos (Sala 01)
- Início com os verbos mais usados do inglês americano
- Template criado: `verbo_template.py` (WeasyPrint + HTML → PDF)
- Estrutura por sentido: cada sentido do verbo gera um PDF separado
- Verbos cobertos: **100 verbos** (#01–100)
- Cada verbo tem: presente (7 pronomes), passado, futuro WILL, futuro GOING TO, negativas e perguntas para cada tempo
- Exemplo de sentido: `BE_Sentido_01_SER.pdf`, `HAVE_Sentido_03_TOMAR.pdf`
- PDFs completos (todos os sentidos unidos): `VERBO_NN_NOME_Completo.pdf`

### Fase 2 — Question Words (Sala 02)
- Template criado: `qw_template.py` (WeasyPrint + HTML → PDF)
- Padrão diferente dos verbos: tabelas de usos com contexto, nota de alerta/dica, comparações
- 8 PDFs gerados: WHO/WHOM/WHOSE, WHAT, WHICH, WHEN, WHERE, WHY, HOW, WHATEVER/WHENEVER/HOWEVER/WHOEVER

### Fase 3 — Conectivos e Conjunções (Sala 02, continuação)
- 9 grupos, 33 PDFs no total, usando o mesmo template `qw_template.py`
- Grupos: Conjunções Básicas, Causa/Resultado, Contraste, Tempo, Adição, Condição, Exemplificação, Sequência/Conclusão, Dia a Dia

### Fase 4 — Gramática Essencial (Sala 03)
- 9 grupos, 35 PDFs
- Conteúdo: Pronomes (4 tipos), Artigos (A/AN/THE/Zero), Modais (6), Preposições de Tempo (4), Preposições de Lugar (3), Preposições de Movimento (3), Advérbios de Frequência (2), Quantificadores (5), Phrasal Verbs (5)

### Fase 5 — Estruturas Fixas / Chunks (Sala 03, continuação)
- 8 PDFs cobrindo blocos fixos de linguagem
- Motivação: aluno tinha dificuldade com estruturas como "What kind of = que tipo de"
- Grupos: HOW + adj, WHAT + noun, IT IS / THERE IS, Tempo fixo, Opinião/Sentimento, Pedido/Educação, Comparação/Intensidade, Causa/Condição fixas

### Fase 6 — Pronúncia e Fala Natural (Sala 04)
- Baseada em áudio transcrito de vídeo educacional
- 4 PDFs: Connected Speech + Flap T, Content vs Function Words, Contractions, Gonna/Wanna/Gotta/Kinda
- Insight central: "não é rapidez, é conexão"

### Fase 7 — Organização e Sequência Lógica
- Criação do ZIP geral com pastas por Sala
- Reorganização em 22 módulos sequenciais com lógica de aprendizado
- Critério de sequência: do mais essencial ao menos essencial, do concreto ao abstrato

---

## 3. ESTRUTURA DE ARQUIVOS GERADOS

### Localização dos outputs
Todos os PDFs foram salvos em: `/mnt/user-data/outputs/`

### Nomenclatura dos arquivos

| Padrão | Tipo | Exemplo |
|--------|------|---------|
| `VERBO_Sentido_NN_TRADUCAO.pdf` | Verbo individual | `BE_Sentido_01_SER.pdf` |
| `VERBO_NN_NOME_Completo.pdf` | Verbo completo | `VERBO_05_GET_Completo.pdf` |
| `QW_PALAVRA_TRADUCAO.pdf` | Question Word | `QW_HOW_COMO_QUANTO_QUAO.pdf` |
| `QW_CONJ_PALAVRA_TRADUCAO.pdf` | Conectivo | `QW_CONJ_AND_E_ADICAO.pdf` |
| `QW_GRAM_GN_NN_PALAVRA_TRADUCAO.pdf` | Gramática | `QW_GRAM_G3_01_CAN_COULD_PODER.pdf` |
| `QW_CHUNK_GN_TEMA_TRADUCAO.pdf` | Chunk/Estrutura Fixa | `QW_CHUNK_G1_HOW_ADJ_HOW_LONG.pdf` |
| `QW_SALA04_PDFn_TEMA_TRADUCAO.pdf` | Sala 04 Pronúncia | `QW_SALA04_PDF1_CONNECTED_SPEECH.pdf` |

### ZIPs entregues

| Arquivo ZIP | Conteúdo |
|-------------|----------|
| `50_Verbos_Ingles_Completo.zip` | Verbos #01–50 |
| `Verbos_51_100_Serie2.zip` | Verbos #51–100 |
| `QW_Question_Words_Completo.zip` | 8 Question Words |
| `Conectivos_Grupo1_Conjuncoes_Basicas.zip` | AND/BUT/OR/SO/YET/NOR/FOR |
| `Conectivos_Grupo2_Causa_Resultado.zip` | BECAUSE/SINCE/THEREFORE/AS A RESULT/DUE TO |
| `Conectivos_Grupo3_Contraste.zip` | HOWEVER/ALTHOUGH/DESPITE/WHEREAS/NEVERTHELESS |
| `Conectivos_Grupo4_Tempo.zip` | WHEN/BEFORE/AFTER/UNTIL/AS SOON AS |
| `Conectivos_Grupo5_Adicao.zip` | ALSO/TOO/IN ADDITION/NOT ONLY...BUT ALSO |
| `Conectivos_Grupo6_Condicao.zip` | IF/UNLESS/PROVIDED THAT/IN CASE/WHETHER |
| `Conectivos_Grupo7_Exemplificacao.zip` | FOR EXAMPLE/IN OTHER WORDS/NAMELY |
| `Conectivos_Grupo8_Sequencia_Conclusao.zip` | FIRST/THEN/FINALLY/IN CONCLUSION |
| `Conectivos_Grupo9_Dia_a_Dia.zip` | ACTUALLY/BY THE WAY/I MEAN/ANYWAY |
| `Gramatica_Essencial_Completa.zip` | 35 PDFs em 9 grupos |
| `Estruturas_Fixas_Chunks_Essenciais.zip` | 8 PDFs de chunks |
| `SALA04_Como_Entender_Nativos.zip` | 4 PDFs pronúncia |
| `Ingles_Brasileiros_COMPLETO.zip` | Tudo em 5 pastas por Sala |
| `Ingles_Sequencia_Logica_22_Modulos.zip` | 237 PDFs em 22 módulos sequenciais |

---

## 4. CONTEÚDO COMPLETO POR SALA

### SALA 01 — Verbos #1–100

**Verbos #01–50:**
BE (6 sentidos), HAVE (17 sentidos), DO (2), GO (6), GET (4), MAKE (4), COME (3), TAKE (3), KNOW (3), THINK (3), SEE (3), WANT (2), GIVE (1), USE (1), FIND (1), TELL (1), ASK (1), ASK FOR (1), WORK (2), SEEM (1), FEEL (1), SAY (2), CALL (2), LEAVE (1), KEEP (1), LET (1), BEGIN (1), SHOW (1), HEAR (1), PLAY (1), RUN (1), MOVE (1), LIVE (1), BELIEVE (1), HOLD (1), BRING (1), HAPPEN (1), WRITE (1), PROVIDE (1), SET (1), MEET (1), STAND (1), INCLUDE (1), CONTINUE (1), LEARN (1), CHANGE (1), LEAD (1), UNDERSTAND (1), TRY (1), LOSE (1), READ (1)

**Verbos #51–100:**
SPEAK, FALL, SEND, SLEEP, DRIVE, SPEND, BREAK, GROW, CHOOSE, OPEN, HELP, TALK, WAIT, BECOME, NEED, LOVE, LIKE, MISS, AGREE, ASK FOR, REMEMBER, FORGET, DECIDE, EXPECT, MEAN, NOTICE, REALIZE, WONDER, WAKE, IMAGINE, COOK, CLEAN, FIX, CHECK, WATCH, BUY, SELL, SAVE, FINISH, START, CUT, BUILD, SHARE, STOP, JOIN, WEAR, FIGHT, CATCH, VISIT, ENJOY

### SALA 02 — Question Words + Conectivos (41 PDFs)

**Question Words (8):** WHO/WHOM/WHOSE, WHAT, WHICH, WHEN, WHERE, WHY, HOW, WHATEVER/WHENEVER/HOWEVER/WHOEVER

**Conectivos (33):** 9 grupos conforme descrito acima

### SALA 03 — Gramática Essencial (35 PDFs)

**Grupo 1 — Pronomes (4):** Sujeito, Objeto, Possessivos, Reflexivos
**Grupo 2 — Artigos (3):** A/AN, THE, Zero Article
**Grupo 3 — Verbos Modais (6):** CAN/COULD, MUST/HAVE TO, SHOULD, MAY/MIGHT, WOULD, WILL/SHALL
**Grupo 4 — Preposições de Tempo (4):** AT, ON, IN, FOR/SINCE/DURING/BY
**Grupo 5 — Preposições de Lugar (3):** IN/ON/AT lugar, posição, distância
**Grupo 6 — Preposições de Movimento (3):** TO/INTO, FROM/OUT OF, THROUGH/ACROSS
**Grupo 7 — Advérbios de Frequência (2):** Always→Never, Every/Once/Twice
**Grupo 8 — Quantificadores (5):** SOME/ANY, MUCH/MANY, A FEW/LITTLE, ENOUGH/TOO, ALL/BOTH/NONE
**Grupo 9 — Phrasal Verbs (5):** GET, GO, TURN/PUT/TAKE, LOOK/FIND/RUN, GIVE/COME/MAKE

### SALA 03 — Estruturas Fixas / Chunks (8 PDFs)

1. HOW + adj (how long/far/old/much/often/soon/tall)
2. WHAT + noun (what kind of, what time, what's it like, what's going on)
3. IT IS / THERE IS / THERE ARE
4. Tempo fixo (as soon as, at first, at last, at least, on time vs in time)
5. Opinião/Sentimento (I think, I feel like, it seems/sounds/looks like)
6. Pedido/Educação (could you, would you mind, I was wondering if)
7. Comparação/Intensidade (as…as, the more…the more, so…that, too…to)
8. Causa/Condição fixas (that's why, even if, no matter what, as long as)

### SALA 04 — Como Entender Nativos que Falam Rápido (4 PDFs)

1. Connected Speech + Flap T — T entre vogais vira R suave ("potato"→"potaro")
2. Content Words vs Function Words — palavras enfatizadas vs reduzidas/inaudíveis
3. Contractions essenciais — I'm/you're/he's/don't/won't/I'll/I've/I'd
4. Gonna/Wanna/Gotta/Kinda + reduções informais (dunno, lemme, gimme, gotcha)

---

## 5. SEQUÊNCIA LÓGICA DE APRENDIZADO (22 Módulos)

A ordem abaixo respeita a progressão cognitiva: concreto → abstrato, essencial → complementar, estrutura → nuance.

| Módulo | Tema | PDFs | Justificativa |
|--------|------|------|---------------|
| 01 | Base Absoluta (Pronomes + BE) | 10 | Sem isso não existe frase |
| 02 | Artigos (A/AN/THE/Zero) | 3 | Erro #1 do brasileiro |
| 03 | Verbos Top 10 (HAVE/DO/GO/GET/MAKE/COME) | 21 | 80% das conversas |
| 04 | Verbos Dia a Dia (KNOW/THINK/SEE/WANT...) | 25 | Ampliação essencial |
| 05 | Verbos Modais (WILL/CAN/MUST/SHOULD...) | 6 | Intenção sobre os verbos |
| 06 | Conectivos Essenciais (AND/BUT/OR/SO/BECAUSE/IF) | 11 | Cola das frases |
| 07 | Question Words (WHO/WHAT/WHEN/WHERE/WHY/HOW) | 8 | Fazer perguntas |
| 08 | Preposições de Tempo (AT/ON/IN/FOR/SINCE) | 4 | Erro gravíssimo e frequente |
| 09 | Preposições de Lugar e Movimento | 6 | Toda frase de contexto físico |
| 10 | Quantificadores e Frequência | 7 | SOME/ANY/MUCH/MANY em toda frase |
| 11 | Estruturas Fixas / Chunks | 8 | Fala natural — blocos prontos |
| 12 | Verbos de Comunicação Social | 13 | SPEAK/TALK/HEAR/SHOW... |
| 13 | Verbos de Rotina e Vida | 15 | WAKE/SLEEP/COOK/READ/DRIVE... |
| 14 | Verbos de Ação e Decisão | 14 | START/STOP/DECIDE/CHOOSE... |
| 15 | Conectivos Intermediários | 11 | SINCE/UNTIL/DESPITE/UNLESS... |
| 16 | Phrasal Verbs | 5 | Essenciais para entender nativos |
| 17 | Verbos de Transação e Trabalho | 12 | BUY/SELL/PAY/SAVE/BUILD... |
| 18 | Conectivos Avançados + Discourse Markers | 12 | WHEREAS/NOT ONLY/ACTUALLY... |
| 19 | Verbos de Sentimento e Percepção | 11 | BELIEVE/NOTICE/REALIZE/WONDER... |
| 20 | Verbos de Movimento Físico | 13 | BRING/HOLD/CATCH/BREAK/WEAR... |
| 21 | Verbos Complementares | 18 | Sentidos secundários de verbos já vistos |
| 22 | Pronúncia e Fala Natural (Sala 04) | 4 | Revisitar com base sólida |

---

## 6. PADRÃO VISUAL DOS PDFs — TEMPLATE COMPLETO

> **INSTRUÇÃO PARA IA:** Este é o template Python completo usado para gerar TODOS os PDFs do projeto (exceto os de Verbos). Para gerar novos PDFs no mesmo padrão, instale WeasyPrint (`pip install weasyprint`) e use o código abaixo como base.

### 6.1 Dependências

```bash
pip install weasyprint --break-system-packages
```

### 6.2 Paleta de Cores (9 rampas)

| Ramp | bg (50) | txt (800) | Uso sugerido |
|------|---------|-----------|--------------|
| Blue | `#E6F1FB` | `#0C447C` | Uso 1 / conceito principal |
| Green | `#EAF3DE` | `#27500A` | Uso 2 / positivo |
| Amber | `#FAEEDA` | `#633806` | Uso 3 / atenção |
| Pink | `#FBEAF0` | `#72243E` | Uso 4 / contraste |
| Purple | `#EEEDFE` | `#3C3489` | Uso 5 / especial |
| Teal | `#E1F5EE` | `#085041` | Uso 6 / extra |
| Red | `#FCEBEB` | `#791F1F` | Uso 7 / erro/perigo |
| Coral | `#FAECE7` | `#993C1D` | Uso 8 / informal |
| Gray | `#F1EFE8` | `#444441` | Uso neutro |

### 6.3 Código completo do template (`qw_template.py`)

```python
from weasyprint import HTML
import os, shutil

os.makedirs('/mnt/user-data/outputs', exist_ok=True)

STYLE = """
<style>
@page { size: A4; margin: 1.6cm 1.4cm; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: Arial, sans-serif;
  font-size: 10.5px;
  color: #1a1a1a;
  background: #fff;
  line-height: 1.5;
}
.page-title {
  font-size: 8.5px;
  color: #bbb;
  text-align: right;
  margin-bottom: 7px;
}
.header {
  border-radius: 10px;
  padding: 13px 16px;
  margin-bottom: 13px;
  display: flex;
  align-items: center;
  gap: 12px;
}
.header-icon {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  color: #fff;
  font-size: 18px;
  font-weight: bold;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.header-title { font-size: 22px; font-weight: bold; }
.header-sub   { font-size: 11px; margin-top: 2px; opacity: 0.85; }

/* Bloco de uso */
.uso-bloco {
  border: 0.5px solid #e0e0e0;
  border-radius: 8px;
  padding: 10px 13px;
  margin-bottom: 10px;
  background: #fcfcfc;
  page-break-inside: avoid;
}
.uso-label {
  font-size: 9.5px;
  font-weight: bold;
  padding: 3px 10px;
  border-radius: 4px;
  display: inline-block;
  margin-bottom: 8px;
}
/* Classes de cor para labels (bg leve + texto escuro da mesma rampa) */
.u1 { background:#E6F1FB; color:#0C447C }
.u2 { background:#EAF3DE; color:#27500A }
.u3 { background:#FAEEDA; color:#633806 }
.u4 { background:#FBEAF0; color:#72243E }
.u5 { background:#EEEDFE; color:#3C3489 }
.u6 { background:#E1F5EE; color:#085041 }
.u7 { background:#FCEBEB; color:#791F1F }
.u8 { background:#FAECE7; color:#993C1D }

/* Tabelas */
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 10px;
  margin-top: 3px;
}
th {
  text-align: left;
  padding: 5px 7px;
  background: #f0f0f0;
  font-weight: bold;
  border-bottom: 1px solid #d8d8d8;
  color: #555;
  font-size: 9.5px;
}
td {
  padding: 5px 7px;
  border-bottom: 0.5px solid #ebebeb;
  vertical-align: top;
}
tr:last-child td { border-bottom: none; }
td:first-child   { font-weight: bold; color: #444; white-space: nowrap; }

/* Notas coloridas */
.alert  { background:#FFF8E1; border-left:3px solid #F6B93B; border-radius:0 5px 5px 0; padding:6px 10px; margin-top:7px; font-size:9.5px; color:#7D4E00; }
.tip    { background:#EBF5FB; border-left:3px solid #2E86C1; border-radius:0 5px 5px 0; padding:6px 10px; margin-top:7px; font-size:9.5px; color:#1A5276; }
.danger { background:#FDEDEC; border-left:3px solid #C0392B; border-radius:0 5px 5px 0; padding:6px 10px; margin-top:7px; font-size:9.5px; color:#7B241C; }
</style>
"""

def tab(cols, rows):
    """Gera tabela HTML a partir de lista de colunas e lista de linhas."""
    h = '<table><tr>' + ''.join(f'<th>{c}</th>' for c in cols) + '</tr>'
    for r in rows:
        h += '<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>'
    return h + '</table>'

def uso(label_class, titulo, rows, cols=None, nota="", nota_class="tip"):
    """Gera um bloco de uso (caixa colorida com tabela e nota opcional)."""
    if cols is None:
        cols = ["Uso / Contexto", "Inglês", "Português"]
    h = f'<div class="uso-bloco"><span class="uso-label {label_class}">{titulo}</span>'
    h += tab(cols, rows)
    if nota:
        h += f'<div class="{nota_class}">{nota}</div>'
    return h + '</div>'

def gerar_qw_html(palavra, icone, bg, txt, traducao, desc,
                  usos,       # lista de tuplas: (label_class, titulo, cols, rows, nota, nota_class)
                  dicas=[]):  # lista de tuplas: (classe, texto)
    """
    Gera o HTML completo de um PDF no padrão QW/Conectivo/Gramática/Chunk.

    Parâmetros:
    - palavra   : título principal (ex: "HOWEVER", "CAN / COULD")
    - icone     : caractere para o círculo do header (ex: "H", "M", "?")
    - bg        : cor de fundo do header (ex: "#E6F1FB")
    - txt       : cor do texto do header (ex: "#0C447C")
    - traducao  : tradução principal (aparece abaixo do título)
    - desc      : descrição curta (subtítulo do header)
    - usos      : lista de blocos de conteúdo
    - dicas     : lista de notas finais (danger/tip)
    """
    h = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head><meta charset="UTF-8">{STYLE}</head>
<body>
<div class="page-title">
  INGLÊS PARA BRASILEIROS | {palavra.upper()} | A1–A2
</div>
<div class="header" style="background:{bg}">
  <div class="header-icon" style="background:{txt}">{icone}</div>
  <div>
    <div class="header-title" style="color:{txt}">{palavra.upper()} = {traducao}</div>
    <div class="header-sub"   style="color:{txt}">{desc}</div>
  </div>
</div>"""

    for (lc, titulo, cols, rows, nota, nc) in usos:
        h += uso(lc, titulo, rows, cols, nota, nc)

    for (tipo, texto) in dicas:
        h += f'<div class="{tipo}">{texto}</div><br>'

    h += "</body></html>"
    return h

def salvar_qw(sufixo, nome_curto, html):
    """Salva o HTML como PDF e copia para /mnt/user-data/outputs/."""
    nome = f"QW_{sufixo}"
    caminho_local = f"/home/claude/{nome}.pdf"
    HTML(string=html).write_pdf(caminho_local)
    destino = f"/mnt/user-data/outputs/{nome}.pdf"
    shutil.copy(caminho_local, destino)
    print(f"  OK {nome}.pdf")
    return destino
```

### 6.4 Exemplo de uso do template

```python
exec(open('/home/claude/qw_template.py').read())

h = gerar_qw_html(
    palavra="HOWEVER",
    icone="H",
    bg="#FBEAF0",       # Pink 50
    txt="#72243E",      # Pink 800
    traducao="NO ENTANTO / POREM",
    desc="Contraste formal entre duas ideias",
    usos=[
        ("u1", "USO 1 — HOWEVER no início da frase",
         ["Estrutura", "Inglês", "Português"],
         [
           ["contraste", "She studied hard. <strong>However</strong>, she failed.", "Ela estudou. No entanto, reprovou."],
           ["contraste", "It's expensive. <strong>However</strong>, it's worth it.", "É caro. No entanto, vale a pena."],
         ],
         "⚠️ HOWEVER precisa de pontuação ao redor. Nunca une duas orações diretamente.",
         "alert"),

        ("u2", "USO 2 — HOWEVER vs BUT",
         ["Palavra", "Registro", "Exemplo"],
         [
           ["BUT",     "informal", "It was hard, but she did it."],
           ["HOWEVER", "formal",   "It was hard. However, she did it."],
         ],
         "💡 Na fala: BUT. Em e-mails e textos formais: HOWEVER.",
         "tip"),
    ],
    dicas=[
        ("danger", "🔴 ERRO COMUM: 'She studied hard, however she failed.' ❌ — use ponto ou ponto e vírgula antes de HOWEVER."),
        ("tip",    "💡 RESUMO: HOWEVER = no entanto (formal) | Sempre com pontuação | Mais formal que BUT."),
    ]
)

salvar_qw("CONJ_HOWEVER_EXEMPLO", "NO_ENTANTO_POREM", h)
```

### 6.5 Estrutura visual detalhada de cada PDF

```
┌─────────────────────────────────────────────────────────────┐
│ INGLÊS PARA BRASILEIROS | PALAVRA | A1–A2          (8.5px) │
├─────────────────────────────────────────────────────────────┤
│ [●]  PALAVRA = TRADUÇÃO                    (22px bold)      │
│      Descrição curta do uso                (11px)           │
├─────────────────────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ USO 1 — TÍTULO                    (label colorida 9.5px)│ │
│ │ ┌──────────────┬──────────────────┬───────────────────┐ │ │
│ │ │ Col 1 (bold) │ Col 2            │ Col 3             │ │ │
│ │ ├──────────────┼──────────────────┼───────────────────┤ │ │
│ │ │ dado         │ dado             │ dado              │ │ │
│ │ └──────────────┴──────────────────┴───────────────────┘ │ │
│ │ ▌ Nota de alerta/dica/perigo           (9.5px, colorida)│ │
│ └─────────────────────────────────────────────────────────┘ │
│ (repete para cada USO)                                      │
├─────────────────────────────────────────────────────────────┤
│ ▌🔴 ERRO COMUM: ...                  (nota danger, 9.5px)  │
│ ▌💡 RESUMO: ...                      (nota tip, 9.5px)     │
└─────────────────────────────────────────────────────────────┘
```

### 6.6 Especificações técnicas detalhadas

| Elemento | Especificação |
|----------|---------------|
| **Página** | A4, margens: 1.6cm top/bottom, 1.4cm left/right |
| **Fonte** | Arial, sans-serif |
| **Corpo do texto** | 10.5px, line-height 1.5, cor #1a1a1a |
| **Page title** | 8.5px, cor #bbb, alinhamento direita |
| **Header** | border-radius 10px, padding 13px 16px, flexbox |
| **Header icon** | 38×38px, border-radius 50% (círculo), fundo = cor txt |
| **Header title** | 22px, bold |
| **Header subtitle** | 11px, opacity 0.85 |
| **Bloco de uso** | border 0.5px #e0e0e0, border-radius 8px, padding 10px 13px, bg #fcfcfc |
| **Label do uso** | 9.5px, bold, padding 3px 10px, border-radius 4px |
| **Tabela** | width 100%, border-collapse collapse, font-size 10px |
| **Cabeçalho da tabela** | bg #f0f0f0, bold, border-bottom 1px #d8d8d8, cor #555, 9.5px |
| **Células** | padding 5px 7px, border-bottom 0.5px #ebebeb |
| **Primeira coluna** | bold, cor #444, white-space nowrap |
| **Nota alert** | bg #FFF8E1, border-left 3px #F6B93B, padding 6px 10px, margin-top 7px, 9.5px, cor #7D4E00 |
| **Nota tip** | bg #EBF5FB, border-left 3px #2E86C1, 9.5px, cor #1A5276 |
| **Nota danger** | bg #FDEDEC, border-left 3px #C0392B, 9.5px, cor #7B241C |
| **Espaço entre blocos** | margin-bottom 10px nos blocos de uso |
| **page-break-inside** | avoid nos blocos de uso |

---

## 7. PADRÃO DOS PDFs DE VERBOS (Template Diferente)

O template de verbos (`verbo_template.py`) tem estrutura diferente do template QW. Cada PDF de verbo contém:

1. **Header colorido** com nome do verbo, tradução e descrição do sentido
2. **Exemplo central** com marcação de cores por papel sintático (VERBO / O QUÊ / A QUEM / ONDE / QUANDO)
3. **Tabela de presente** — 7 pronomes (I/YOU/HE/SHE/IT/WE/THEY) com exemplos
4. **Tabela de passado**
5. **Tabela de futuro WILL**
6. **Tabela de futuro GOING TO**
7. **Tabelas de negativas** — presente, passado, will, going to
8. **Tabelas de perguntas** — presente, passado, will, going to
9. **Notas de erro** (vermelho) e **dicas** (azul)

---

## 8. DECISÕES PEDAGÓGICAS TOMADAS

### Princípios que guiaram o projeto

1. **Do essencial ao complementar** — sempre começar pelos itens mais frequentes
2. **Por sentido, não por palavra** — cada sentido de um verbo tem seu próprio PDF
3. **Afirmativo + Negativo + Pergunta** — todos os três modos em cada tempo verbal
4. **Presente + Passado + Futuro** — cobertura temporal completa
5. **Alertas de erros do brasileiro** — erros específicos do falante nativo do português
6. **Comparações entre palavras similares** — ex: ALTHOUGH vs EVEN THOUGH vs THOUGH
7. **Exemplos reais e contextualizados** — não frases artificiais de gramática
8. **Estruturas fixas antes de regras** — chunks prontos para usar, depois a teoria
9. **Pronúncia como complemento** — Sala 04 aborda o que é difícil de ouvir

### Descobertas durante o projeto

- A dificuldade com estruturas como "What kind of" levou à criação da categoria Chunks
- O áudio de professor revelou que a dificuldade com nativos é de "conexão de sons", não de velocidade
- A reorganização em 22 módulos mostrou que muitos PDFs estavam na ordem subótima para aprendizado

---

## 9. CONTINUIDADE SUGERIDA — PRÓXIMOS PASSOS

### Conteúdos não gerados ainda

| Categoria | Sugestão |
|-----------|----------|
| **Sala 05 — Gramática Avançada** | Reported speech, conditionals (if type 1/2/3), passive voice |
| **Sala 06 — Vocabulário Temático** | Casa, trabalho, saúde, viagem, restaurante, compras |
| **Sala 07 — Expressões Idiomáticas** | As 50 mais usadas no inglês americano |
| **Sala 08 — Inglês de Negócios** | E-mails, reuniões, negociação, apresentações |
| **Sala 09 — Gírias Americanas** | As mais usadas em séries e filmes |
| **Flashcards** | Versão reduzida (frente/verso) dos PDFs para revisão rápida |
| **Áudios** | Gravações dos exemplos para treino de listening |

### Melhorias técnicas possíveis

- Adicionar QR code em cada PDF linkando para pronúncia no Forvo ou YouGlish
- Criar versão "modo noturno" dos PDFs (fundo escuro)
- Adicionar numeração de página e índice nos PDFs completos
- Criar app de flashcards baseado nos PDFs gerados

---

## 10. INSTRUÇÃO PARA CONTINUAR O PROJETO COM NOVA IA

Se você é uma IA lendo este documento para continuar o projeto, aqui está o que precisa saber:

### Ambiente de geração
- **OS:** Ubuntu 24 (Linux)
- **Python:** 3.x
- **Biblioteca PDF:** WeasyPrint (`from weasyprint import HTML`)
- **Diretório de trabalho:** `/home/claude/`
- **Diretório de saída:** `/mnt/user-data/outputs/`

### Como gerar um novo PDF
1. Salve o template (seção 6.3) como `/home/claude/qw_template.py`
2. Crie um script Python que faça `exec(open('/home/claude/qw_template.py').read())`
3. Chame `gerar_qw_html(...)` com os parâmetros desejados
4. Chame `salvar_qw(sufixo, nome_curto, html)` para salvar
5. O PDF aparecerá em `/mnt/user-data/outputs/QW_{sufixo}.pdf`

### Nomenclatura a seguir
- Novos PDFs de gramática: `QW_GRAM_G{n}_{nn}_{PALAVRA}_{TRADUCAO}.pdf`
- Novos conectivos: `QW_CONJ_{PALAVRA}_{TRADUCAO}.pdf`
- Novas salas: `QW_SALA0{n}_PDF{n}_{TEMA}_{TRADUCAO}.pdf`

### Paleta de cores padrão (rotação sugerida)
Use `u1` a `u8` nos blocos de uso, rotacionando as cores do padrão.
Para o header, escolha uma cor da paleta da seção 6.2 baseada no tema.

---

## 11. ESTATÍSTICAS DO PROJETO

| Métrica | Valor |
|---------|-------|
| Total de PDFs gerados | ~260 |
| Verbos cobertos | 100 |
| Sentidos de verbos | ~170 |
| Question Words | 8 |
| Conectivos/Conjunções | 33 |
| PDFs de Gramática | 35 |
| PDFs de Chunks | 8 |
| PDFs de Pronúncia | 4 |
| Módulos sequenciais | 22 |
| ZIPs entregues | 17+ |
| Sessões de trabalho | 7+ sessões |
| Período do projeto | Abril 2026 |

---

## 12. CRÉDITOS E CONTEXTO

- **Usuário:** Brasileiro residente no Rio de Janeiro, nível A1→A2 de inglês
- **Plataforma de geração:** Claude (Anthropic) — claude.ai
- **Modelo:** Claude Sonnet 4.6
- **Ferramenta de PDF:** WeasyPrint (Python)
- **Inspiração para Sala 04:** Vídeo de professor de inglês no Instagram sobre como nativos falam rápido
- **Metodologia:** "Prompt Universal — Inglês para Brasileiros" — criada e refinada ao longo das sessões

---

*Documento gerado automaticamente a partir do histórico completo das sessões de trabalho. Última atualização: Maio de 2026.*
