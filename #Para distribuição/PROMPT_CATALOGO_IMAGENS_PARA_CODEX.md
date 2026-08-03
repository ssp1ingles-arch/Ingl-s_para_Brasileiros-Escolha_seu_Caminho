# Tarefa: extrair e catalogar todo o conteúdo de inglês das imagens

Trabalhe no projeto:

`C:\Users\Samukk99\Documents\Claude Code Projetos\Inglês para Brasileiros - Escolha seu Caminho`

Pasta de origem:

`C:\Users\Samukk99\Documents\Claude Code Projetos\Inglês para Brasileiros - Escolha seu Caminho\#Para distribuição`

## Objetivo

Leia visualmente **cada uma das 333 imagens atualmente existentes** na pasta `#Para distribuição` (331 PNG e 2 JPG), extraia todo conteúdo útil de inglês e reúna o resultado em **um único catálogo Markdown completo, organizado, pesquisável e rastreável**.

Arquivo final obrigatório:

`#Para distribuição\CATALOGO_CONTEUDO_INGLES.md`

Não crie um Markdown por imagem. O produto final é um catálogo único.

## Contexto obrigatório antes de começar

1. Leia integralmente `REGRAS_GERAIS.md`.
2. Leia `#Para distribuição\README.md`.
3. O README registra que 188 imagens do lote `IMG_6520.PNG` a `IMG_6714.PNG` já alimentaram painéis do projeto. Mesmo assim, elas devem aparecer no catálogo para garantir inventário completo e rastreabilidade, mas devem ser marcadas como `lote anteriormente implementado`.
4. Há 145 imagens adicionais fora daquele lote histórico, incluindo arquivos anteriores a `IMG_6520` e imagens posteriores a `IMG_6714`.
5. Antes de sugerir um Sistema de destino, leia o `REGRAS.md` específico desse Sistema.

## Regras de extração

- Inspecione a imagem de verdade com visão e OCR; não classifique apenas pelo nome do arquivo.
- Preserve fielmente o inglês apresentado: frases, diálogos, expressões, vocabulário, phrasal verbs, exemplos, contrastes, tabelas e estruturas gramaticais.
- Preserve traduções ou explicações curtas em português quando elas fizerem parte útil do material original.
- Corrija somente erros evidentes de OCR. Não reescreva, simplifique ou invente conteúdo.
- Se um trecho não puder ser lido com segurança, registre `[trecho ilegível]` e a imagem de origem; não adivinhe.
- Descarte elementos sem valor didático: interface do Instagram, curtidas, comentários, nomes de botões, horários, bateria, chamadas promocionais, links, hashtags, propaganda e pedidos para seguir/comentar/compartilhar.
- Não inclua dicas de estudo, motivação, metodologia ou conselhos genéricos como conteúdo de inglês.
- Imagens puramente visuais, promocionais ou sem inglês útil devem continuar no inventário com o motivo da exclusão.
- Nunca desperdice conteúdo útil. Uma imagem pode alimentar mais de uma categoria ou Sistema.
- Detecte sequências de carrossel e agrupe as imagens relacionadas quando isso melhorar a compreensão, mantendo todos os nomes de origem.
- Detecte duplicatas exatas e quase duplicatas. Mantenha uma entrada canônica e liste todas as imagens duplicadas, sem repetir o conteúdo desnecessariamente.

## Estrutura obrigatória do catálogo

Comece o arquivo com:

1. Título e data da auditoria.
2. Resumo executivo.
3. Totais: imagens encontradas, lidas, com conteúdo útil, sem conteúdo útil, duplicadas, ilegíveis e pertencentes ao lote já implementado.
4. Índice por tema.
5. Índice por Sistema sugerido.

Depois organize o conteúdo por grandes temas, por exemplo:

- Gramática e estruturas
- Vocabulário e expressões
- Verbos e phrasal verbs
- Inglês real, reduções e pronúncia
- Conectores e question words
- Preposições, tempo e localização
- Diálogos e situações práticas
- Dúvidas e contrastes frequentes
- Outros conteúdos úteis
- Imagens descartadas ou sem texto útil

Para cada entrada, use este modelo:

```markdown
### CAT-0001 — Título descritivo

- **Imagem(ns) de origem:** `IMG_0000.PNG`
- **Situação da fonte:** nova | lote anteriormente implementado
- **Tema:**
- **Nível estimado:** A1 | A2 | B1 | B2 | C1 | misto
- **Sistema(s) sugerido(s):** S01, S02 etc.
- **Tipo:** frase | diálogo | vocabulário | expressão | tabela | gramática | pronúncia | outro
- **Status:** aproveitável | duplicata | parcial | ilegível | descartada

#### Conteúdo em inglês

[transcrição estruturada e fiel]

#### Apoio em português existente na imagem

[somente o que já estiver na fonte e for útil]

#### Observações

[contexto, relação com outras imagens, duplicatas e eventuais dúvidas]
```

Não acrescente tradução própria quando a imagem não trouxer tradução. Não transforme o catálogo em aula nova.

## Forma de trabalho e checkpoints

- Processe em ordem natural de nome de arquivo.
- Trabalhe em lotes pequenos, preferencialmente de 15 a 25 imagens, para evitar perda de progresso.
- Após cada lote, atualize o mesmo `CATALOGO_CONTEUDO_INGLES.md` e a tabela de controle no início do arquivo.
- Pode usar arquivos temporários em `tmp\imagens_catalogo`, mas não entregue arquivos intermediários como resultado final.
- Não declare uma imagem como lida sem inspeção visual ou saída de OCR/visão verificável.
- Se houver interrupção, deixe no topo do catálogo o último arquivo concluído e o próximo arquivo a processar.

## Validação final obrigatória

Antes de encerrar:

1. Refaça o inventário da pasta e confirme que todas as 333 imagens aparecem no catálogo, individualmente ou dentro de um grupo claramente enumerado.
2. Confirme que nenhum nome de arquivo foi omitido ou repetido indevidamente.
3. Confirme que todas as entradas possuem imagem de origem e status.
4. Confirme que duplicatas apontam para uma entrada canônica.
5. Confirme que itens ilegíveis ou descartados possuem justificativa.
6. Procure resíduos de OCR, caracteres corrompidos e linhas absurdamente longas.
7. Informe os totais finais e quaisquer pontos que ainda exijam revisão humana.

## Limites da tarefa

- Não alterar HTML, CSS, JavaScript, `sistemas.json`, PDFs ou arquivos dos Sistemas.
- Não mover, renomear nem apagar as imagens de origem.
- Não distribuir ou implementar o conteúdo nos painéis nesta etapa; apenas sugerir destinos no catálogo.
- Não alterar `README.md`.
- Não realizar commit nem push.
- Continue até catalogar todas as imagens; não peça confirmação entre lotes.

Ao concluir, relate o caminho do catálogo, os totais auditados, os descartes, as duplicatas, os trechos ilegíveis e o próximo passo recomendado para distribuição nos Sistemas.
