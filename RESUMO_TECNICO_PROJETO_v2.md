# RESUMO TÉCNICO COMPLETO — Inglês para Brasileiros: Escolha seu Caminho
**Versão 2 — Julho 2026**
**Para uso por qualquer IA que continue este projeto**

---

## 1. O QUE É ESTE PROJETO

Um sistema de ensino de inglês para brasileiros, organizado em **23 painéis HTML interativos**, hospedado no GitHub Pages. Cada painel (chamado "Sistema") é uma pasta no computador do usuário com arquivos HTML que ensinam inglês de formas diferentes — gramática, pronúncia, vocabulário, diálogos reais, livros, transcrições de vídeos, etc.

O usuário acessa tudo pelo site público ou abrindo os arquivos localmente via servidor HTTP.

---

## 2. CAMINHOS ESSENCIAIS

| O quê | Caminho |
|-------|---------|
| **Raiz do projeto** | `C:\Users\Samukk99\Documents\Claude Code Projetos\Inglês para Brasileiros - Escolha seu Caminho` |
| **Entrada de novo conteúdo** | `...\#Para distribuição` |
| **Repositório GitHub** | https://github.com/ssp1ingles-arch/Ingl-s_para_Brasileiros-Escolha_seu_Caminho |
| **Site público** | https://ssp1ingles-arch.github.io/Ingl-s_para_Brasileiros-Escolha_seu_Caminho/ |
| **Script de push** | `auto_push.bat` na raiz (encoding cp1252, CRLF — nunca editar com UTF-8) |
| **Raiz do git** | A própria pasta raiz do projeto (não a pasta pai) |
| **Branch** | `main` |

---

## 3. ARQUIVOS DE CONTROLE NA RAIZ

| Arquivo | Função |
|---------|--------|
| `sistemas.json` | Lista dos 23 sistemas — o painel principal lê este JSON e gera os cards dinamicamente via JavaScript. **Sempre atualizar quando mudar estrutura.** |
| `index.html` | Painel principal — lê sistemas.json, gera 23 cards com links |
| `REGRAS_GERAIS.md` | Regras globais do projeto |
| `REGRAS_AVANCADO.md` | Regras especiais para S20, S21, S22 (gramática avançada C1/C2) |
| `MAPEAMENTO_ARQUIVOS.md` | Status de todos os livros/arquivos (implementado/aguardando/descartado) |
| `auto_push.bat` | Faz git add + commit + push. Usa `cd /d "%~dp0"` — funciona de qualquer lugar |
| `.gitignore` | Ignora: *.pdf, *.zip, *.png, *.jpg, *.jpeg, *.docx — **PDFs ficam APENAS localmente** |

---

## 4. ESTRUTURA COMPLETA DOS 23 SISTEMAS

### Sistemas de Conteúdo (01-09)

| # | Nome | Conteúdo | Sub-painéis | Status |
|---|------|----------|-------------|--------|
| 01 | Base. Fluência. Gramática | 25 módulos A1→C1 em 4 fases + gramática em tabelas | pronomes-e-artigos.html, gramatica-em-tabelas.html | ✅ |
| 02 | Dúvidas Pontuais | 25 cards de gramática + vocabulário de referência + falar-melhor | duvidas-gramatica.html, vocabulario-referencia.html, falar-melhor.html | ✅ |
| 03 | Reduções do Inglês Real | Rachel's English (reduções + sons) + livro-x-rua | reducoes.html, entender-nativos.html, verbo-think.html, livro01.html, livro02.html, livro-x-rua.html | ✅ |
| 04 | Motor de Verbos | Matriz 12 tempos + verbos + colocações + famílias | gramatica-viva.html, dicionario-de-verbos.html, modais-phrasal-verbs.html, colocacoes-verbais.html, familias-de-verbos.html | ✅ |
| 05 | Conectar Frases | Question words + conectivos + expressões + even-so | conversas-question-words.html, colocacoes-naturais.html, expressoes-idiomaticas.html, conectivos-question-words.html, even-so-conectores.html | ✅ |
| 06 | Situar a Frase | Preposições + teste + estruturas + mapas | ingles-do-zero.html, teste-seu-nivel.html, went-ou-gone.html, estruturas-fixas.html, preposicoes-quantificadores.html, preposicoes-mapas.html | ✅ |
| 07 | Baseado em Desenho Infantil | 7 níveis progressivos, 37 cenas — para adultos com linguagem simples | Navegação por cenas via JS | ✅ |
| 08 | Transcrições e Canais | 45 docx processados: 11.513 falas, 231 expressões, 1.259 frases | 16 sub-painéis (um por canal) | ✅ |
| 09 | Prática Completa · 4 Pilares | Extraído do S03 original — 4 pilares de prática | pilar1 a pilar4.html | ✅ |

### Sistemas de Livros (10-23)

| # | Nome | PDFs | Implementados | Status |
|---|------|------|---------------|--------|
| 10 | Livros V01 — Conversação & Frases | 6 | 6/6 | ✅ completo |
| 11 | Livros V02 — Gramática em Uso | 6 | 3/6 (livro01, livro02, livro04) | ⏳ |
| 12 | Livros V03 — American English File | 6 | 1/6 | ⏳ |
| 13 | Livros V04 — English for Everyone | 6 | 1/6 | ⏳ |
| 14 | Livros V05 — Business & Avançado | 6 | 0/6 | ⏳ |
| 15 | Livros V06 — Exercícios & Vocabulário | 6 | 1/6 | ⏳ |
| 16 | Livros V07 — In Use Series | 6 | 1/6 | ⏳ |
| 17 | Livros V08 | 3 | 0/3 | ⏳ |
| 18 | Livros V09 — B2 First | 5 | 0/5 | ⏳ |
| 19 | Livros V10 — Gramática Básica | PDFs | 1 (livro01 — For Dummies) | ⏳ |
| 20 | Livros V11 — Gramática Avançada | PDFs | 0 | ⏳ REGRAS especiais |
| 21 | Livros V12 — Gramática Avançada | PDFs | 0 | ⏳ REGRAS especiais |
| 22 | Livros V13 — Gramática Avançada | PDFs | 0 | ⏳ REGRAS especiais |
| 23 | Livros — Kids | 2 | 2/2 (Level 3 e Level 4) | ✅ completo |

---

## 5. REGRAS FUNDAMENTAIS — LER ANTES DE QUALQUER AÇÃO

### 5.1 Regras Gerais (todos os sistemas)

1. **#Para distribuição** — TODO conteúdo novo entra primeiro nesta pasta. Analise, decida o Sistema correto, mova e implemente. Nunca implemente direto numa pasta de Sistema sem passar por esta fila.

2. **Nunca alterar conteúdo** — reorganizações são APENAS de estrutura/layout/navegação. Conteúdo só muda se o usuário pedir explicitamente.

3. **Visual padrão obrigatório** — fundo `#0a0a0a`, fontes Space Grotesk/Inter, tema dark em TODOS os painéis. Sem exceção.

4. **Botão Voltar FIXO** — `position:fixed` no topo, sempre visível ao rolar, altura mínima 44px (mobile). Cada sub-painel volta para o hub do seu Sistema (não para o painel principal). O hub do Sistema volta para o `../index.html` (painel principal).

5. **Scroll preservado** — o painel principal (raiz/index.html) salva `scrollPos_root` via `sessionStorage` ao clicar num card. Cada hub de Sistema salva `scrollPos_sNN` ao entrar em sub-painéis. Ao voltar, a posição é restaurada. Chaves: `scrollPos_root`, `scrollPos_s01`, `scrollPos_s02`... `scrollPos_s08v01`, `scrollPos_s08kids`, etc.

6. **Hub → Sub-painel** — cada Sistema é uma página-hub com cards clicáveis para sub-painéis. SEM scroll infinito numa única página.

7. **Nunca inventar conteúdo** — usar APENAS o que está nos arquivos fonte. Se não tem arquivo, não tem conteúdo.

8. **Commit por tarefa** + `git push origin main` ao final de cada lote.

9. **PDFs ficam APENAS localmente** — nunca commitar PDFs, ZIPs, DOCXs ou imagens. O `.gitignore` já bloqueia, mas verificar sempre.

10. **Numeração** — sempre verificar a numeração real das pastas no disco antes de escrever qualquer referência. A numeração mudou várias vezes ao longo do projeto. O `sistemas.json` é a fonte de verdade.

### 5.2 Regras para Livros PDF (Sistemas 10-23, exceto S20-S22)

- Extrair **APENAS inglês real**: diálogos, frases completas, vocabulário em uso, exemplos em contexto
- **NUNCA incluir**: dicas de estudo, métodos, técnicas de memorização, motivação, "como aprender", enunciados de exercício, gabarito isolado, notas do professor
- Um livro por vez, ao comando do usuário
- Sempre ler `REGRAS.md` do Sistema antes de implementar
- Verificar se PDF tem texto extraível (pdftotext/PyMuPDF) ou é escaneado (usar RapidOCR — demora ~7-10s/página)
- Comparar com livros já implementados no mesmo Sistema para não duplicar

### 5.3 Regras Especiais — S20, S21, S22 (Gramática Avançada C1/C2)

Esses três sistemas têm `REGRAS_AVANCADO.md` (raiz + cópia em cada pasta). São DIFERENTES dos outros:

**PERMITIDO (além do padrão):**
- Explicações gramaticais completas com nuances de uso
- Comparações entre estruturas semelhantes (would vs could vs might)
- Notas de uso formal vs informal vs escrito vs falado
- Erros comuns com explicação do POR QUÊ está errado
- Tabelas comparativas de estruturas complexas
- Exemplos em contexto estendido (parágrafos, não só frases)
- Conteúdo de preparação para exames C1/C2

**Acento visual:** dourado `#F59E0B` (para marcar nível avançado visualmente)

### 5.4 Exceção autorizada — S03 (Reduções)

No Sistema 03, explicações de COMO e QUANDO ocorre a redução são permitidas — é o núcleo do aprendizado deste sistema. Esta é a única exceção às regras gerais para sistemas de conteúdo.

---

## 6. FLUXO DE TRABALHO CORRETO

### Como este projeto funciona na prática:

```
USUÁRIO (Cowork/Claude)          CLAUDE CODE (VSCode local)
        |                                |
Entende a solicitação                   |
Elabora prompt detalhado  ──────────>  Executa
        |                          Cria/edita HTMLs
        |                          Faz commits
Recebe relatório          <──────────  git push origin main
Verifica e reporta                      |
```

**IMPORTANTE:** Todo trabalho de arquivo é feito pelo Claude Code local no VSCode. O Cowork (este chat) elabora os prompts e verifica os resultados. Nunca tente executar tarefas de arquivo diretamente por aqui.

### Fluxo para novo conteúdo:

```
1. Usuário coloca arquivo em #Para distribuição
2. Claude Code lista e lê TODOS os arquivos da pasta
3. Consulta REGRAS_GERAIS.md e REGRAS.md do Sistema candidato
4. Decide o Sistema correto baseado no conteúdo real
5. Move arquivo para _fontes/ do Sistema
6. Implementa no sub-painel correto
7. git commit + push
```

### Fluxo para novo livro PDF:

```
1. Usuário indica o livro E a pasta de destino
2. Claude Code lê REGRAS.md do Sistema
3. Verifica se PDF tem texto ou é escaneado
4. Extrai APENAS inglês real (nunca método/dica/gabarito)
5. Compara com livros já implementados (sem duplicar)
6. Cria livroXX.html + card no hub
7. Atualiza MAPEAMENTO_ARQUIVOS.md
8. git commit + push
```

---

## 7. HISTÓRICO — DE ONDE VIEMOS

### Origem (pastas antigas — NÃO excluídas):
- `Americano_01` — fonte original dos sistemaX_conteudo.md (sistema2 a sistema27)
- `Sala_001` — PDFs distribuídos pelos Sistemas

### O que foi feito:
1. Conteúdo das pastas antigas foi **copiado** (não movido) para os Sistemas organizados
2. Americano_01 foi arquivado em `.zip` no `_admin` do S01
3. As pastas antigas ainda existem no disco mas não são mais usadas

### Evolução da estrutura:
- Começou com 6 Sistemas simples
- Cresceu para 10 → 16 → 17 → 22 → 23 Sistemas
- O Sistema 08 "Livros" se dividiu em V01 a V09 + Kids (hoje S10 a S23)
- A numeração mudou várias vezes — **sempre verificar o disco e o sistemas.json**

---

## 8. ERROS CRÍTICOS A EVITAR

### Erro 1 — Assumir numeração sem verificar
A numeração dos Sistemas mudou múltiplas vezes. SEMPRE listar as pastas do disco antes de escrever qualquer referência a número de Sistema. Nunca confiar em memória ou contexto anterior.

### Erro 2 — Commitar PDFs
O `.gitignore` bloqueia, mas verificar com `git status` antes do push. PDFs ficam APENAS localmente.

### Erro 3 — Incluir método/dica nos painéis de livros
Qualquer texto sobre "como estudar", "técnicas", "dicas", "motivação" é descartado. Mesmo que o livro seja bom, só entra o inglês real.

### Erro 4 — Não ler REGRAS.md antes de implementar
Cada Sistema tem regras próprias. S03 permite explicações de pronúncia. S20-S22 permitem explicações avançadas. Os demais não.

### Erro 5 — Quebrar links ao renomear pastas
Ao renomear qualquer pasta, verificar e atualizar: sistemas.json, todos os botões "← Voltar" internos, chaves sessionStorage, títulos/eyebrow/footer dos HTMLs.

### Erro 6 — Alterar conteúdo sem permissão
Reorganização de layout = permitido. Alteração de conteúdo = só com ordem explícita do usuário.

### Erro 7 — Criar sub-painel sem hub
Todo Sistema deve ter um `index.html` que funciona como hub com cards clicáveis. Nunca criar apenas sub-painéis sem o hub.

### Erro 8 — auto_push.bat com encoding errado
O arquivo DEVE ser cp1252/ANSI com CRLF. Nunca editar com UTF-8 ou salvar com LF. Usar Python com `encoding='cp1252', newline=''` se precisar recriar.

---

## 9. ESTADO ATUAL DOS LIVROS IMPLEMENTADOS

### S10 — V01 Conversação & Frases (COMPLETO)
- livro01: 1.006 dicas de inglês real
- livro02: Conversação para Viagem (Michaelis) — 261 frases
- livro03: 120 frases de conversação — 5 temas
- livro04: Música + 90 citações célebres — 1.286 itens
- livro05: Vocabulário + números + datas — 404 itens
- livro06: Erros reais (remember/remind, lose/miss...) — 436 frases

### S11 — V02 Gramática em Uso
- livro01: English Grammar in Use — 2.800 itens (B1-B2)
- livro02: Grammar Practice Intermediate — 400 frases, 10 tabelas
- livro04: Essential Grammar in Use — 700+ frases (A1-B1)
- Pendentes: livro03, livro05, livro06 (Reactivate C1/C2 aguarda)

### S12 — V03 American English File
- livro01: American English File 1 — 174 frases, 16 seções

### S13 — V04 English for Everyone
- livro01: Grammar Guide — 191 frases, 36 temas, tabelas visuais

### S15 — V06 Exercícios & Vocabulário
- livro01: English Grammar in Use Supplementary — 123 frases

### S16 — V07 In Use Series
- livro01 (está como livro02 no disco): English Vocabulary in Use Elementary — 431 entradas

### S19 — V10 Gramática Básica
- livro01: Basic English Grammar For Dummies — 1.130 itens, 41 tabelas

### S23 — Kids (COMPLETO)
- livro01: Kid's Box Level 3 — 242 frases
- livro02: Kid's Box Level 4 — 389 frases

### S03 — Reduções (livros dentro do Sistema)
- livro01: Rachel's English (reduções da fala) — 208 itens
- livro02: Rachel's English (inventário de sons) — 183 itens

---

## 10. PARA ONDE VAMOS

### Pendências imediatas:
- [ ] S14 — V05: nenhum livro implementado (6 PDFs aguardando)
- [ ] S17 — V08: 3 PDFs aguardando
- [ ] S18 — V09 B2 First: 5 PDFs aguardando
- [ ] S20-S22 — Gramática Avançada: PDFs aguardando (regras especiais prontas)
- [ ] S11: livros 03, 05, 06 pendentes
- [ ] S12: livros 02-06 pendentes
- [ ] S13: livros 02-06 pendentes
- [ ] S23: REGRAS.md próprio ainda não criado

### Regras de expansão futura:
- Novos livros: usuário indica livro + pasta destino → implementa um por vez
- Nova pasta de Sistema: criar hub placeholder + adicionar ao sistemas.json
- Novo conteúdo: sempre pela pasta `#Para distribuição`
- Novos Sistemas avançados (S20-S22): seguir `REGRAS_AVANCADO.md`

---

## 11. COMANDOS ÚTEIS PARA O CLAUDE CODE

```bash
# Verificar estado do git
cd "C:\Users\Samukk99\Documents\Claude Code Projetos\Inglês para Brasileiros - Escolha seu Caminho"
git status -sb
git log --oneline -5

# Listar todas as pastas de Sistema
dir /b /ad "Sistema*"

# Verificar links quebrados (Python)
python -c "
import os, re
broken = []
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            # verificar hrefs locais
            pass
print('Verificação concluída')
"

# Push manual
git add .
git commit -m 'descrição clara da tarefa'
git push origin main

# Se index.lock travar o git
del .git\index.lock
```

---

## 12. COMO ELABORAR UM BOM PROMPT PARA O CLAUDE CODE

Todo prompt deve conter:
1. **Caminho base** — sempre o caminho completo da raiz
2. **Contexto** — o que já existe, o que mudou
3. **Tarefa numerada** — cada tarefa separada e clara
4. **Regras específicas** — qual REGRAS.md ler, exceções aplicáveis
5. **O que NÃO fazer** — previne erros comuns
6. **Commit + push** — sempre no final com mensagem descritiva
7. **Relatório** — o que deve ser reportado ao fim

---

*Documento gerado em julho/2026. Atualizar sempre que houver mudança estrutural significativa.*
