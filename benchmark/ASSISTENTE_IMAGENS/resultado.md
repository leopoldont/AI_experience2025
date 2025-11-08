# RESULTADO DO BENCHMARK: ASSISTENTE DE GERAÇÃO DE IMAGENS

Este arquivo documenta os resultados gerados por um modelo de IA para cada um dos três tipos de prompt.

---

## 1. Resposta ao Prompt Genérico

**Prompt:** `Crie uma imagem.`

**Resultado:**

Eu adoraria! Para que eu possa gerar a descrição de uma imagem incrível para você, por favor, me diga:

**O que você quer que eu crie?**

Seja o mais descritivo possível. Pense em:
*   **Sujeito:** O que ou quem é o foco principal? (Ex: um dragão, uma cidade futurista, uma floresta mágica)
*   **Ação:** O que está acontecendo na imagem? (Ex: voando, dormindo, brilhando)
*   **Cenário:** Onde a cena se passa?
*   **Estilo:** Qual estilo visual você prefere? (Ex: fotorrealista, aquarela, cartoon, cyberpunk, fantasia)

Quanto mais detalhes, melhor!

---

## 2. Resposta ao Prompt Estruturado (JSON)

**Prompt:**
```json
{
  "task": "gerar_imagem_com_ia",
  "context": {
    "background": "Um designer precisa de uma imagem conceitual para uma campanha de marketing.",
    "user_goal": "Gerar uma imagem fotorrealista de um astronauta surfando em um anel de Saturno."
  },
  "instructions": {
    "elements": [
      "**Sujeito principal:** Um astronauta com traje espacial branco e detalhes em dourado.",
      "**Ação:** O astronauta está em uma prancha de surfe, em uma pose dinâmica.",
      "**Cenário:** Os anéis de Saturno, que se parecem com uma onda cósmica.",
      "**Iluminação:** Luz dramática vinda de uma estrela distante, criando sombras longas.",
      "**Estilo:** Fotorrealismo, alta definição, com texturas detalhadas no traje e na prancha."
    ],
    "output_format": "Imagem em alta resolução (16:9)."
  },
  "constraints": [
    "A imagem não deve conter texto ou marcas d'água.",
    "O rosto do astronauta deve estar coberto pelo capacete.",
    "Foco na composição épica e cinematográfica."
  ],
  "user_input": "Quero uma imagem de um astronauta surfando nos anéis de Saturno."
}
```

**Resultado:**

**Prompt de Imagem Gerado (Pronto para ser usado em uma IA de imagem):**

"Fotorrealismo, alta definição, composição épica e cinematográfica. Um astronauta em uma pose de surfe dinâmica, deslizando sobre uma onda cósmica formada pelos anéis de Saturno. O traje espacial é branco com detalhes em dourado, exibindo texturas complexas e reflexos. A iluminação é dramática, com uma luz forte vinda de uma estrela distante, projetando sombras longas e realçando os detalhes da cena. O rosto do astronauta está completamente obscurecido pelo visor do capacete. Proporção da imagem 16:9."

---

## 3. Resposta ao Prompt Estruturado (KERNEL)

**Prompt:**
- **K (Keep it simple):** Gerar uma imagem de um astronauta surfando nos anéis de Saturno.
- **E (Easy to verify):** A imagem deve conter um astronauta, uma prancha de surfe e os anéis de Saturno em estilo fotorrealista.
- **R (Reproducible results):** O prompt descreve os elementos visuais de forma consistente.
- **N (Narrow scope):** A tarefa é focada na geração de uma única imagem.
- **E (Explicit constraints):** Estilo fotorrealista, sem texto, rosto coberto, proporção 16:9.
- **L (Logical structure):**
    1.  **Task:** Gerar uma imagem fotorrealista de um astronauta surfando no espaço.
    2.  **Input:** Astronauta com traje branco/dourado, prancha de surfe, anéis de Saturno como onda, iluminação dramática.
    3.  **Constraints:** Fotorrealismo, alta definição, sem texto, proporção 16:9.
    4.  **Output:** Arquivo de imagem em alta resolução.
    5.  **Verify:** Checar se a imagem gerada corresponde à descrição, estilo e restrições.

**Resultado:**

**Prompt de Imagem Gerado (Pronto para ser usado em uma IA de imagem):**

"Imagem fotorrealista em alta definição, estilo cinematográfico, de um astronauta com um traje espacial branco e dourado, surfando em uma prancha. O cenário são os anéis de Saturno, que se comportam como uma onda gigante e cósmica. A cena é iluminada por uma luz dramática de uma estrela distante, criando um forte contraste e sombras alongadas. O capacete do astronauta esconde completamente seu rosto. A composição deve ser épica, sem nenhum texto ou marca d'água. Formato widescreen 16:9."
