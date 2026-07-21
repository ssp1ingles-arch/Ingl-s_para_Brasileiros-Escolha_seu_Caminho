# Sistema 09 — Dúvidas Pontuais
**Plataforma:** Inglês para Brasileiros (`ssp1ingles-arch.github.io/americano_01`)
**Cor de acento:** Laranja `#F97316`
**Ícone:** 🎯
**Subtítulo:** "Gramática sob medida — os pontos que você quis dominar"

---

## Estrutura de Arquivos

```
output/sistema06/
  index.html          ← hub com grid de cards
  did/
    index.html        ← página completa sobre DID
  went/
    index.html        ← página completa sobre WENT
```

---

## Itens atuais

### 1. DID (A1 — Auxiliar)
- O que é: passado do verbo DO; não muda para nenhuma pessoa
- 4 funções: Perguntas / Negações / Verbo principal / Ênfase
- Regra de Ouro: quando DID aparece como auxiliar, o verbo principal volta para a forma base (não vai ao passado)
- Tabela de erros comuns: Did you **went**? → Did you **go**? / I didn't **saw** → I didn't **see**

### 2. WENT (A1 — Irregular)
- O que é: passado irregular de GO; nunca é auxiliar
- Regra de Ouro: WENT só aparece em frases afirmativas. Em negativas e perguntas, o verbo volta para GO
- Tabela de erros comuns: I didn't **went** → I didn't **go** / Did you **went**? → Did you **go**?

---

## Detalhes Técnicos

| Item | Detalhe |
|---|---|
| localStorage | `s06_progress` — marca `p.<slug>=true` ao abrir cada item |
| Badge "✓ visto" | Aparece no card do hub após a primeira visita |
| Links internos | Páginas → hub do S06 (`../index.html`) → Painel raiz (`../../index.html`) |
| nav.js | Mantido sem alteração (dropdown ainda lista sistemas antigos 1–27) |
| Quiz/exercícios | Não incluídos — sistema é de referência rápida |
| Deploy | Manual via `auto_push.bat` — sem automação |

---

## Painel Principal (output/index.html)
- Card adicionado: "🎯 06 — Dúvidas Pontuais" com subtítulo "DID, WENT e mais"
- Subtítulo geral atualizado: "Cinco sistemas" → "Seis sistemas"
- Variável CSS adicionada: `--s06-accent: #F97316`

---

## Próximos Itens Sugeridos
- WAS vs WERE
- HAVE vs HAS
- BEEN
- CAN vs COULD
- DO vs DOES

---

## Status
✅ Criado e validado — aguardando `auto_push.bat` para publicação
