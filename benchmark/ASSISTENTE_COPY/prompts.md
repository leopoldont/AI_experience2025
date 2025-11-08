# PROMPTS PARA ASSISTENTE DE COPYWRITING

---

## 1. Prompt Genérico

Escreva uma copy para meu anúncio.

---

## 2. Prompt Estruturado (JSON)

```json
{
  "task": "criar_copy_para_anuncio",
  "context": {
    "background": "A campanha é para o lançamento de um novo curso online de fotografia para iniciantes.",
    "user_goal": "Gerar uma copy persuasiva para um anúncio no Instagram, com foco em conversão."
  },
  "instructions": {
    "steps": [
      "Escrever uma headline que chame a atenção em menos de 10 palavras.",
      "Desenvolver um corpo de texto que destaque os 3 principais benefícios do curso.",
      "Criar uma chamada para ação (CTA) clara e direta para 'inscreva-se agora'.",
      "Incluir 3 hashtags relevantes."
    ],
    "output_format": "Texto curto e direto, ideal para feed do Instagram, com quebras de linha para facilitar a leitura."
  },
  "constraints": [
    "O texto completo não deve ultrapassar 150 palavras.",
    "Usar uma linguagem energética e motivacional.",
    "Evitar promessas exageradas."
  ],
  "user_input": "O curso ensina a usar qualquer câmera, até mesmo a do celular."
}
```

---

## 3. Prompt Estruturado (KERNEL)

- **K (Keep it simple):** Criar a copy para um anúncio de Instagram de um curso de fotografia.
- **E (Easy to verify):** A copy deve ter menos de 150 palavras, uma headline, 3 benefícios, um CTA e 3 hashtags.
- **R (Reproducible results):** O prompt é autocontido e não depende de dados externos voláteis.
- **N (Narrow scope):** A tarefa é focada apenas na criação da copy do anúncio.
- **E (Explicit constraints):** Limite de 150 palavras, linguagem energética, sem promessas exageradas.
- **L (Logical structure):**

    1.  **Task:** Gerar uma copy persuasiva para um anúncio no Instagram.
    2.  **Input:** Lançamento de um curso online de fotografia para iniciantes.
    3.  **Constraints:** Máximo de 150 palavras. Linguagem motivacional. CTA para 'inscreva-se agora'.
    4.  **Output:** Texto curto para Instagram com headline, 3 benefícios, CTA e 3 hashtags.
    5.  **Verify:** Conferir o limite de palavras, a estrutura e a presença de todos os elementos solicitados.
