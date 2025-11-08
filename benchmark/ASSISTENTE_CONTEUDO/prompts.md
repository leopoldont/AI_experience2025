# PROMPTS PARA ASSISTENTE DE CONTEÚDO

---

## 1. Prompt Genérico

Escreva um post para meu blog.

---

## 2. Prompt Estruturado (JSON)

```json
{
  "task": "criar_post_para_blog",
  "context": {
    "background": "O blog é sobre marketing digital para pequenas empresas.",
    "user_goal": "Gerar um artigo otimizado para SEO sobre a importância do marketing de conteúdo."
  },
  "instructions": {
    "steps": [
      "Escrever um título atraente e otimizado para a palavra-chave 'marketing de conteúdo'.",
      "Desenvolver uma introdução que prenda a atenção do leitor.",
      "Estruturar o corpo do texto em 3 seções principais com subtítulos.",
      "Incluir uma conclusão com uma chamada para ação (CTA) para 'assinar a newsletter'.",
      "O texto deve ter no mínimo 800 palavras."
    ],
    "output_format": "Texto em formato Markdown, pronto para ser publicado."
  },
  "constraints": [
    "A palavra-chave 'marketing de conteúdo' deve aparecer pelo menos 5 vezes.",
    "Evitar jargões técnicos excessivos.",
    "O tom deve ser educativo e acessível."
  ],
  "user_input": "O público-alvo são empreendedores que não têm muito conhecimento de marketing."
}
```

---

## 3. Prompt Estruturado (KERNEL)

- **K (Keep it simple):** Criar um post de blog sobre a importância do marketing de conteúdo.
- **E (Easy to verify):** O post deve ter no mínimo 800 palavras, um título, 3 seções com subtítulos, uma conclusão com CTA e a palavra-chave principal repetida 5 vezes.
- **R (Reproducible results):** O prompt não depende de informações sazonais.
- **N (Narrow scope):** A tarefa é focada apenas na redação de um único post.
- **E (Explicit constraints):** Mínimo de 800 palavras, 5 menções à palavra-chave, tom educativo, evitar jargões.
- **L (Logical structure):**

    1.  **Task:** Criar um post de blog otimizado para SEO sobre a importância do marketing de conteúdo.
    2.  **Input:** Blog sobre marketing digital para pequenas empresas.
    3.  **Constraints:** Mínimo de 800 palavras. Usar a palavra-chave 'marketing de conteúdo' 5 vezes. Tom acessível.
    4.  **Output:** Texto em formato Markdown.
    5.  **Verify:** Checar a contagem de palavras, o uso da palavra-chave, a estrutura de subtítulos e a presença do CTA.
