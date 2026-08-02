# Progresso da conversão sequencial de PDFs

Atualizado em: 2026-08-01

## Concluído e auditado

- Sistema 16 — Baseado em Livros V07: 6 de 6 livros.
  - 1.757 páginas textuais, 78.180 linhas e 2.864.956 bytes.
- Sistema 15 — Baseado em Livros V06: 6 de 6 livros.
  - 1.202 páginas textuais, 78.984 linhas e 2.433.900 bytes.
- Sistema 14 — Baseado em Livros V05: 6 de 6 livros.
  - 1.374 páginas textuais, 71.775 linhas e 1.835.885 bytes.
- Sistema 13 — Baseado em Livros V04: 6 de 6 livros.
  - Livro 01: 361 páginas textuais, 10.979 linhas e 422.999 bytes.
  - Livro 02: 361 páginas textuais, 18.059 linhas e 244.775 bytes.
  - Livro 03: 256 páginas textuais, 7.407 linhas e 100.122 bytes.
  - Livro 04: 176 páginas textuais, 9.851 linhas e 183.603 bytes.
  - Livro 05: 184 páginas textuais, 9.668 linhas e 192.896 bytes.
  - Livro 06: 357 páginas textuais, 16.096 linhas e 349.952 bytes.
- Sistema 12 — Baseado em Livros V03: 6 de 6 livros.
  - Livro 01: 166 páginas textuais, 16.430 linhas e 382.371 bytes; página 166 vazia confirmada visualmente.
  - Livro 02: 169 páginas textuais, 16.708 linhas e 439.819 bytes.
  - Livro 03: 168 páginas textuais, 16.669 linhas e 491.737 bytes.
  - Livro 04: 169 páginas textuais, 18.459 linhas e 595.838 bytes; página 168 quase vazia confirmada visualmente.
  - Livro 05: 193 páginas textuais, 10.948 linhas e 517.556 bytes.
  - Livro 06: 216 páginas textuais, 16.776 linhas e 588.102 bytes.
- Sistema 11 — Baseado em Livros V02: 5 de 6 livros (o livro 06 foi excluído do escopo por orientação do usuário).
  - Livro 01: 392 páginas textuais, 22.688 linhas e 957.087 bytes; páginas 2 e 393 vazias confirmadas visualmente.
  - Livro 02: 174 páginas textuais, 8.806 linhas e 231.562 bytes.
  - Livro 03: 453 páginas textuais, 21.352 linhas e 900.055 bytes; página 1 (capa, OCR de baixa confiança) confirmada visualmente.
  - Livro 04: 299 páginas textuais, 14.065 linhas e 630.757 bytes; nenhuma página exigiu OCR.
  - Livro 05: 325 páginas analisadas, 320 com texto, 18.038 linhas e 407.707 bytes; PDF totalmente digitalizado (OCR nas 325 páginas). As 5 páginas sem texto (15, 93, 95, 125 e 127) foram confirmadas visualmente como folhas em branco do scan. A página 56 (menor confiança, 0,703) foi conferida visualmente: a prosa está íntegra; a confiança baixa vem dos marcadores fonéticos minúsculos (`[u]`, `[ʊ]`) sobrescritos às palavras, que o OCR isola em linhas curtas ao longo de todo o livro.

Todos os livros acima foram validados sem resíduos `(cid:n)`, sem U+FFFD, sem linhas acima de 500 caracteres e sem páginas duplicadas. As páginas vazias e as páginas de menor confiança foram verificadas visualmente quando aplicável.

## Ponto exato de retomada

Trabalho parado aguardando nova orientação do usuário.

O Sistema 11 — Baseado em Livros V02 está encerrado dentro do escopo definido: os livros 01 a 05 foram convertidos e auditados; o livro `06_Reactivate Your Grammar And Vocabulary C1C2 - Exams.pdf` não deve ser convertido (orientação do usuário em 2026-08-02).

A sequência prevista adiante era Sistemas 10, 09 e 08, um livro por vez com auditoria antes de avançar — mas só retomar após confirmação do usuário.

## Restrições mantidas

- Nenhum HTML deve ser alterado.
- Nenhum PDF deve ser renomeado, alterado ou removido.
- Nenhum commit ou push deve ser realizado.
- O conversor e a pasta de checkpoints devem ser preservados enquanto houver livros pendentes.
