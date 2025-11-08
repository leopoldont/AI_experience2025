# PROMPTS PARA ASSISTENTE DE GERAÇÃO DE IMAGENS

---

## 1. Prompt Genérico

Crie uma imagem.

---

## 2. Prompt Estruturado (JSON)

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

---

## 3. Prompt Estruturado (KERNEL)

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
