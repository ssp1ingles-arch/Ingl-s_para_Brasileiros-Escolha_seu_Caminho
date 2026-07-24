# REGRAS_AVANCADO — Sistemas 19, 20 e 21 · Gramática Avançada

> Leia também o `REGRAS_GERAIS.md` na raiz. **Este arquivo substitui as regras de livro dos demais Sistemas** para S19, S20 e S21 — e só para eles.

---

## 0. A quem se aplica

| Sistema | Pasta | Livros |
|---|---|---|
| **S19** | `Sistema 19 — Baseado em Livros V10 Gramática Avançada` | 7 |
| **S20** | `Sistema 20 — Baseado em Livros V11 Gramática Avançada` | 5 |
| **S21** | `Sistema 21 — Baseado em Livros V12 Gramática Avançada` | 3 |

Nenhum outro Sistema segue estas regras. Um livro que sair de S19/S20/S21 volta a seguir as regras do Sistema de destino.

## 1. Por que estas regras são diferentes

Nos demais Sistemas de livros a regra é dura: **só inglês real, zero explicação**. Isso funciona porque o aluno ali está montando a base — ele precisa de frase pronta, não de teoria.

No nível avançado o problema muda. Quem chega em C1/C2 já sabe formar a frase; o que trava é **a nuance**: por que `would` e não `could`, por que essa estrutura soa formal demais numa conversa, por que o nativo escreve assim mas nunca fala assim. **Nesse nível a explicação é o conteúdo** — sem ela, sobra só uma lista de frases sem o que as diferencia.

Público destes três Sistemas: **quem já tem base sólida.** Quem ainda está construindo deve ir aos Sistemas 01, 04, 11 e 15 primeiro.

## 2. O que É PERMITIDO aqui (e não é nos outros Sistemas)

- **Explicações gramaticais completas, com nuance de uso.** Não a regra decorada — o que a estrutura faz com o sentido da frase.
- **Comparações entre estruturas semelhantes.** `would` × `could` × `might`; `I wish` × `if only`; `used to` × `would` × `be used to`; particípio × gerúndio em oração reduzida. Sempre lado a lado, com o que muda em cada uma.
- **Notas de registro:** formal × informal, escrito × falado, britânico × americano, acadêmico × conversacional. Dizer explicitamente onde cada forma cabe e onde soa errada.
- **Erros comuns com o POR QUÊ.** Nunca só "está errado": mostrar a forma errada, a correta e a razão da diferença (regra de estrutura, colocação, registro ou lógica de sentido).
- **Tabelas comparativas** de estruturas complexas — condicionais mistas, inversão, tempos perfeitos, verbos com padrão de complemento (`remember doing` × `remember to do`).
- **Exemplos em contexto estendido:** parágrafos, trechos de diálogo longo, textos curtos — não só frases soltas. No avançado a estrutura só se prova em contexto.
- **Conteúdo de preparação para exames (C1/C2)** quando o livro trouxer: linguagem de *essay*, *report*, *proposal*, *review*, conectores de argumentação, paráfrase e reformulação.

## 3. O que se MANTÉM (vale aqui como em todo o projeto)

- **Sempre inglês real, com exemplo completo.** Nenhuma explicação entra sozinha: cada ponto precisa da frase (ou do parágrafo) que o demonstra.
- **Nunca gabarito isolado** (`1-b, 2-c, 3-a`) nem **enunciado de exercício puro** (`Complete the sentences with…`). Se a frase do exercício é inglês real, ela entra completa e resolvida; a instrução do exercício, não.
- **Nunca** dica de estudo, método do autor, motivação ou "como aprender inglês" — isso continua fora, como no `REGRAS_GERAIS.md` §4.
- **Visual dark padrão** do projeto (`REGRAS_GERAIS.md` §2), com **acento dourado `#F59E0B`** nos três Sistemas — o dourado é a marca visual do nível avançado.
- **Do menos ao mais complexo dentro de cada livro.** A ordem é pedagógica, não a ordem de página do PDF.
- Botão **"← Voltar ao início"** → `../index.html` (`REGRAS_GERAIS.md` §3).

## 4. Formato do painel de livro (`livroNN.html`)

Estrutura sugerida por ponto de gramática:

1. **Título do ponto** — o nome da estrutura, em inglês.
2. **A explicação** — o que ela faz com o sentido. Curta e específica, não a definição de dicionário.
3. **Exemplos** — em contexto; parágrafo quando o ponto exigir.
4. **Comparação** — a estrutura vizinha que se confunde com essa, lado a lado (tabela quando forem 3+).
5. **Registro** — onde cabe: falado, escrito, formal, acadêmico.
6. **Erro comum** — forma errada → forma certa → por quê.

Nem todo ponto precisa dos seis blocos. Precisam sempre: **explicação + exemplo real**.

## 5. Numeração dos arquivos-fonte

Os PDFs seguem o prefixo `01_`, `02_`… na ordem oficial do Sistema. **Pendência conhecida:** quatro PDFs do S20 e os três do S21 ainda estão sem prefixo — a ordem oficial é a dos cards no `index.html` de cada Sistema, e os arquivos devem ser renomeados quando forem implementados.

## 6. Commits

Um commit por livro implementado, no padrão do projeto: `feat(S19): <nome do livro> — livroNN`.
