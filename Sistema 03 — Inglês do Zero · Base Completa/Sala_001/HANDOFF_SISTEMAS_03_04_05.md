# HANDOFF — Sistemas 03, 04 e 05
**Inglês para Brasileiros · ssp1ingles-arch.github.io/americano_01**
**Fonte de dados:** `Sala_001/_FONTE_LIMPA/`
**Data:** 2026-07-19

---

## ANTES DE COMEÇAR — LEITURA DOS PDFs

Os PDFs foram gerados por um template Python (WeasyPrint) com estrutura consistente.
Para cada PDF, tente extrair o texto com:

```python
import pdfplumber

with pdfplumber.open("caminho/do/arquivo.pdf") as pdf:
    for page in pdf.pages:
        print(page.extract_text())
```

Se pdfplumber não estiver disponível: `pip install pdfplumber`

Os nomes dos arquivos já revelam o conteúdo (ex: `08_UNDERSTAND_Entender.pdf`).
Se a extração de texto falhar em algum PDF, use o nome do arquivo como fonte do conteúdo e preencha com o conhecimento gramatical correto — o template é previsível.

**Estrutura típica de cada PDF (Motor de Verbos):**
- Verbo + sentido + tradução PT
- Tabela: 7 pronomes × presente / passado / futuro WILL / futuro GOING TO
- Cada célula: afirmativo + negativo + pergunta
- Seção "Erro típico do brasileiro"

---

## SISTEMA 03 — Motor de Verbos por Sentido

**Pasta fonte:** `Sala_001/_FONTE_LIMPA/Sistema_03_Verbos/` (142 PDFs)
**Destino:** `output/sistema03/`
**Cor de acento:** `#6366F1` (índigo)
**Nível:** A2–B1
**Ícone:** ⚡

### 3.1 Página principal: `output/sistema03/index.html`

```html
<!-- Breadcrumb: ← Painel Principal / Sistema 03 -->
<!-- Título: Motor de Verbos por Sentido -->
<!-- Subtítulo: 100 verbos. Cada sentido. Cada tempo. Afirmativo, negativo e pergunta. -->

<!-- Stats -->
<div class="stats-row">
  <div><strong>100</strong><span>Verbos</span></div>
  <div><strong>~170</strong><span>Sentidos</span></div>
  <div><strong>3</strong><span>Tempos</span></div>
  <div><strong>3</strong><span>Formas</span></div>
</div>

<!-- Navegação por categoria semântica (5 grupos) -->
```

**5 grupos de verbos para a navegação:**

| Grupo | Verbos incluídos | Arquivo destino |
|---|---|---|
| Ter, Fazer, Ir | HAVE (14 sentidos), DO, GO, GET | `grupo1/index.html` |
| Dizer, Pensar, Saber | SAY, TELL, THINK, KNOW, MEAN, UNDERSTAND, REMEMBER, FORGET | `grupo2/index.html` |
| Sentir, Querer, Precisar | FEEL, WANT, NEED, LIKE, LOVE, ENJOY, MISS | `grupo3/index.html` |
| Agir, Mover, Criar | TAKE, MAKE, COME, GIVE, FIND, LEAVE, RUN, BUILD, LEAD, MOVE | `grupo4/index.html` |
| Rotina e Vida | WAKE, SLEEP, COOK, WATCH, PLAY, DRIVE, LEARN, START, STOP, WORK, LIVE, + demais | `grupo5/index.html` |

### 3.2 Formato das páginas de grupo: `output/sistema03/grupo1/index.html`

**FORMATO NOVO — Não existe em nenhum sistema atual:**

Interface de 3 colunas:
1. **Coluna esquerda:** lista de verbos do grupo (clicável)
2. **Coluna central:** lista de sentidos do verbo selecionado (clicável)
3. **Coluna direita:** tabela de conjugação completa

```javascript
// Estrutura de dados a ser preenchida após ler os PDFs
const verbos = {
  "HAVE": {
    sentidos: [
      {
        num: "01",
        pt: "TER (posse)",
        exemplo: "I have a car.",
        tabela: {
          I:    { presente: ["I have","I don't have","Do I have?"],
                  passado:  ["I had","I didn't have","Did I have?"],
                  futuro_will: ["I will have","I won't have","Will I have?"],
                  futuro_going: ["I'm going to have","I'm not going to have","Am I going to have?"] },
          You:  { /* mesmo padrão */ },
          He:   { /* mesmo padrão */ },
          She:  { /* mesmo padrão */ },
          It:   { /* mesmo padrão */ },
          We:   { /* mesmo padrão */ },
          They: { /* mesmo padrão */ }
        },
        erro_brasileiro: "❌ 'I have hunger' ✅ 'I'm hungry' — em inglês, fome e sede são adjetivos, não posses."
      },
      // sentidos 02 a 14...
    ]
  },
  "DO": { /* mesmo padrão */ },
  // demais verbos do grupo...
}
```

**HTML da tabela de conjugação:**

```html
<div class="conj-table">
  <div class="conj-header">
    <div class="col-pronoun">Pronome</div>
    <div class="col-tense">Presente</div>
    <div class="col-tense">Passado</div>
    <div class="col-tense">Futuro WILL</div>
    <div class="col-tense">Futuro GOING TO</div>
  </div>
  <!-- Para cada pronome: -->
  <div class="conj-row" data-pronoun="I">
    <div class="pronoun-cell">I</div>
    <div class="tense-cell">
      <div class="form affirm">I have</div>
      <div class="form neg">I don't have</div>
      <div class="form question">Do I have?</div>
    </div>
    <!-- demais tempos -->
  </div>
  <!-- demais pronomes -->

  <!-- Seção de erro -->
  <div class="erro-box">
    <span class="erro-label">⚠️ Erro típico do brasileiro</span>
    <p>[conteúdo do PDF]</p>
  </div>
</div>
```

**CSS das 3 formas (cores diferentes):**
```css
.form.affirm   { color: #4ade80; }  /* verde — afirmativo */
.form.neg      { color: #f87171; }  /* vermelho — negativo */
.form.question { color: #60a5fa; }  /* azul — pergunta */
```

### 3.3 Progresso

localStorage key: `s03_progress`
Marcar como concluído por sentido (não por verbo inteiro).
Barra de progresso no topo de cada grupo: X de Y sentidos concluídos.

---

## SISTEMA 04 — Conectar Frases

**Pasta fonte:** `Sala_001/_FONTE_LIMPA/Sistema_04_QW_Conectivos/` (42 PDFs)
**Destino:** `output/sistema04/`
**Cor de acento:** `#10B981` (esmeralda)
**Nível:** A2–B1
**Ícone:** 🔗

### 4.1 Página principal: `output/sistema04/index.html`

```html
<!-- Título: Conectar Frases -->
<!-- Subtítulo: Question Words, conectivos e marcadores de fala — o que une ideias em inglês -->

<!-- Stats -->
<div class="stats-row">
  <div><strong>8</strong><span>Question Words</span></div>
  <div><strong>22</strong><span>Conectivos</span></div>
  <div><strong>12</strong><span>Discourse Markers</span></div>
  <div><strong>3</strong><span>Módulos</span></div>
</div>
```

**3 módulos:**

| Módulo | Conteúdo | Arquivo |
|---|---|---|
| Módulo 1 — Perguntar | WHO, WHAT, WHEN, WHERE, WHY, HOW, WHICH, WHATEVER/WHENEVER | `perguntar/index.html` |
| Módulo 2 — Conectar | AND, BUT, OR, SO, BECAUSE, IF, WHEN/WHILE, BEFORE/AFTER, ALTHOUGH, + intermediários (SINCE, UNTIL, UNLESS, DESPITE, THEREFORE, HOWEVER, IN ADDITION, FOR EXAMPLE, IN CONCLUSION, FIRST/THEN/FINALLY, ALSO/TOO) | `conectar/index.html` |
| Módulo 3 — Falar Naturalmente | Discourse markers: WHEREAS, NEVERTHELESS, NOT ONLY BUT ALSO, DUE TO, PROVIDED/IN CASE, YET, NOR, FOR (formal), IN OTHER WORDS, ACTUALLY, BY THE WAY + outros | `falar/index.html` |

### 4.2 FORMATO NOVO — Construtor de Frase

**Não existe em nenhum sistema atual.**

Para cada conectivo/question word, exibir um **construtor interativo de frase:**

```html
<div class="conector-card">
  <div class="conector-word">BECAUSE</div>
  <div class="conector-pt">porque / pois</div>
  <div class="conector-uso">Liga causa e consequência. Responde à pergunta "por quê?"</div>

  <!-- Construtor de frase -->
  <div class="frase-builder">
    <div class="parte-a">
      <label>Resultado</label>
      <select class="frase-select" data-slot="A">
        <option>I stayed home</option>
        <option>She was happy</option>
        <option>We cancelled the trip</option>
      </select>
    </div>
    <div class="conector-fixo">because</div>
    <div class="parte-b">
      <label>Causa</label>
      <select class="frase-select" data-slot="B">
        <option>it was raining</option>
        <option>she passed the test</option>
        <option>the weather was bad</option>
      </select>
    </div>
  </div>

  <!-- Frase montada em tempo real -->
  <div class="frase-resultado">
    I stayed home <strong>because</strong> it was raining.
  </div>

  <!-- Tradução -->
  <div class="frase-traducao">Eu fiquei em casa porque estava chovendo.</div>

  <!-- Erro típico -->
  <div class="erro-box">
    ⚠️ "Because of" precisa de substantivo, não de frase:
    ✅ "Because of the rain" ❌ "Because of it was raining"
  </div>

  <!-- Botão concluir -->
  <button class="btn-concluir">✓ Entendi</button>
</div>
```

**JS simples para montar a frase em tempo real:**
```javascript
document.querySelectorAll('.frase-select').forEach(select => {
  select.addEventListener('change', () => {
    const a = document.querySelector('[data-slot="A"]').value;
    const b = document.querySelector('[data-slot="B"]').value;
    document.querySelector('.frase-resultado').innerHTML =
      `${a} <strong>because</strong> ${b}.`;
  });
});
```

### 4.3 Progresso

localStorage key: `s04_progress`
Marcar por conectivo. Barra de progresso por módulo.

---

## SISTEMA 05 — Situar a Frase

**Pasta fonte:** `Sala_001/_FONTE_LIMPA/Sistema_05_Prep_Quant_Chunks/` (23 PDFs)
**Destino:** `output/sistema05/`
**Cor de acento:** `#EC4899` (rosa)
**Nível:** A2–B1
**Ícone:** 📍

### 5.1 Página principal: `output/sistema05/index.html`

```html
<!-- Título: Situar a Frase -->
<!-- Subtítulo: Preposições, quantificadores e estruturas fixas — onde, quando, quanto e como -->

<!-- Stats -->
<div class="stats-row">
  <div><strong>8</strong><span>Preposições</span></div>
  <div><strong>9</strong><span>Quantificadores</span></div>
  <div><strong>8</strong><span>Chunks</span></div>
  <div><strong>3</strong><span>Módulos</span></div>
</div>
```

**3 módulos:**

| Módulo | PDFs | Arquivo |
|---|---|---|
| Módulo 1 — Preposições | AT/ON/IN tempo, IN/ON/AT lugar, Near/Far/Through, From/Out of, Through/Across, FOR/SINCE/DURING, AS SOON AS, + 1 movimento | `preposicoes/index.html` |
| Módulo 2 — Quantificadores e Frequência | SOME/ANY, MUCH/MANY/A LOT OF, ALL/BOTH/NONE/EACH/EVERY, A FEW/A LITTLE, ENOUGH/TOO, Freq. ADV (always→never), EVERY/ONCE/TWICE | `quantificadores/index.html` |
| Módulo 3 — Chunks e Estruturas Fixas | IT IS/THERE IS, HOW LONG/FAR/OLD/MUCH, WHAT KIND OF/TIME/LIKE, I THINK/FEEL LIKE/IT SEEMS, COULD YOU/WOULD YOU MIND, AS...AS/THE MORE/SO THAT, THAT'S WHY/EVEN IF/NO MATTER | `chunks/index.html` |

### 5.2 FORMATO NOVO — Antes e Depois + Situação Visual

**Não existe em nenhum sistema atual.**

**Para Preposições — Card de contraste PT↔EN:**

```html
<div class="prep-card">
  <div class="prep-title">AT · ON · IN — Tempo</div>

  <!-- Contraste visual em 3 colunas -->
  <div class="prep-grid">
    <div class="prep-col" data-prep="AT">
      <div class="prep-label">AT</div>
      <div class="prep-regra">Momentos precisos</div>
      <ul class="prep-exemplos">
        <li>at 3 o'clock</li>
        <li>at noon</li>
        <li>at night</li>
        <li>at Christmas</li>
      </ul>
      <div class="prep-dica">🎯 Horas e eventos pontuais</div>
    </div>
    <div class="prep-col" data-prep="ON">
      <div class="prep-label">ON</div>
      <div class="prep-regra">Dias e datas</div>
      <ul class="prep-exemplos">
        <li>on Monday</li>
        <li>on July 4th</li>
        <li>on my birthday</li>
        <li>on weekends</li>
      </ul>
      <div class="prep-dica">🗓️ Dias específicos</div>
    </div>
    <div class="prep-col" data-prep="IN">
      <div class="prep-label">IN</div>
      <div class="prep-regra">Períodos longos</div>
      <ul class="prep-exemplos">
        <li>in the morning</li>
        <li>in July</li>
        <li>in 2024</li>
        <li>in summer</li>
      </ul>
      <div class="prep-dica">📅 Meses, anos, estações</div>
    </div>
  </div>

  <!-- Erro típico do brasileiro -->
  <div class="erro-box">
    ⚠️ "in Monday" não existe. Dias da semana = ON.
    ⚠️ "on the morning" não existe. Partes do dia = IN (exceto "at night").
  </div>

  <!-- Mini-quiz de fixação -->
  <div class="quiz-inline">
    <p>Complete: "She was born ___ 1995, ___ a Monday, ___ 6 AM."</p>
    <button class="quiz-reveal">Ver resposta</button>
    <div class="quiz-answer" style="display:none">
      in 1995 · on a Monday · at 6 AM
    </div>
  </div>
</div>
```

**Para Chunks — Card de "bloco pronto":**

```html
<div class="chunk-card">
  <div class="chunk-label">ESTRUTURA FIXA</div>
  <div class="chunk-formula">IT IS + adjetivo + TO + verbo</div>

  <div class="chunk-exemplos">
    <div class="chunk-ex">It is <em>easy</em> to learn.</div>
    <div class="chunk-ex">It is <em>important</em> to practice.</div>
    <div class="chunk-ex">It is <em>hard</em> to explain.</div>
  </div>

  <div class="chunk-pt">
    PT: É fácil aprender. / É importante praticar.
  </div>

  <div class="chunk-armadilha">
    ❌ "Is easy learn" — em inglês, precisa do IT IS + TO
  </div>

  <!-- Expander: mais exemplos -->
  <button class="btn-mais">+ Ver mais exemplos</button>
</div>
```

### 5.3 Progresso

localStorage key: `s05_progress`
Marcar por card/preposição/chunk. Barra de progresso por módulo.

---

## ATUALIZAR: `output/index.html` (Painel Principal)

Adicionar os 3 novos portais ao grid existente:

```html
<!-- Portal 03 — substituir o "Em Breve" -->
<a href="sistema03/index.html" class="portal-card" data-sistema="03">
  <div class="portal-num">03</div>
  <div class="portal-icon">⚡</div>
  <h2 class="portal-title">Motor de Verbos por Sentido</h2>
  <p class="portal-desc">100 verbos, 170 sentidos. Cada verbo no tempo certo — afirmativo, negativo e pergunta.</p>
  <div class="portal-meta">
    <span>5 grupos</span><span>A2–B1</span><span>142 verbos-sentido</span>
  </div>
  <div class="portal-cta">Entrar →</div>
</a>

<!-- Portal 04 -->
<a href="sistema04/index.html" class="portal-card" data-sistema="04">
  <div class="portal-num">04</div>
  <div class="portal-icon">🔗</div>
  <h2 class="portal-title">Conectar Frases</h2>
  <p class="portal-desc">Question words, conectivos e discourse markers — o que liga ideias em inglês.</p>
  <div class="portal-meta">
    <span>3 módulos</span><span>A2–B1</span><span>42 conectores</span>
  </div>
  <div class="portal-cta">Entrar →</div>
</a>

<!-- Portal 05 -->
<a href="sistema05/index.html" class="portal-card" data-sistema="05">
  <div class="portal-num">05</div>
  <div class="portal-icon">📍</div>
  <h2 class="portal-title">Situar a Frase</h2>
  <p class="portal-desc">Preposições, quantificadores e estruturas fixas — onde, quando, quanto e como.</p>
  <div class="portal-meta">
    <span>3 módulos</span><span>A2–B1</span><span>23 estruturas</span>
  </div>
  <div class="portal-cta">Entrar →</div>
</a>
```

**CSS — adicionar acento para os novos portais:**
```css
.portal-card[data-sistema="03"] { --accent-for-this-card: #6366F1; }
.portal-card[data-sistema="04"] { --accent-for-this-card: #10B981; }
.portal-card[data-sistema="05"] { --accent-for-this-card: #EC4899; }
```

---

## SEQUÊNCIA DE IMPLEMENTAÇÃO

```
1. Ler todos os PDFs de Sistema_03_Verbos/ e extrair conteúdo
2. Criar output/sistema03/ (hub + 5 grupos de verbos)
3. Ler todos os PDFs de Sistema_04_QW_Conectivos/ e extrair conteúdo
4. Criar output/sistema04/ (hub + 3 módulos)
5. Ler todos os PDFs de Sistema_05_Prep_Quant_Chunks/ e extrair conteúdo
6. Criar output/sistema05/ (hub + 3 módulos)
7. Atualizar output/index.html (substituir "Em Breve" + adicionar portais 04 e 05)
8. Verificar todos os links de volta ao painel
9. Não rodar auto_push.bat — deixar para revisão manual
```

**Importante:** Construir um sistema completo por vez. Não paralelizar.
Começar pelo Sistema 03 (o maior e mais valioso).

---

## REGRAS GERAIS

- **Não repetir formatos** do Sistema 01 (cards de lição, frases crescentes) ou Sistema 02 (cards de redução, treino de transcrição)
- **Sempre do mais fácil para o mais avançado** dentro de cada módulo
- **Erros do brasileiro** em todo card que tiver essa informação no PDF
- **localStorage separado** por sistema (s03, s04, s05) — nunca misturar
- **Sem auto_push** — publicação manual após revisão

---

*Documento gerado em 19/07/2026 — Colar no Claude Code após staging confirmado*
