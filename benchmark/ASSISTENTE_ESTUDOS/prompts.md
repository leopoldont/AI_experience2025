# PROMPTS PARA ASSISTENTE DE ESTUDOS

---

## 1. Prompt Genérico

Me ajude a estudar.

---

## 2. Prompt Estruturado (JSON)

```json
{
  "task": "criar_plano_de_estudos_e_resumo",
  "context": {
    "background": "Um estudante precisa de ajuda para se preparar para uma prova de história.",
    "user_goal": "Gerar um plano de estudos semanal e um resumo sobre a Revolução Francesa."
  },
  "instructions": {
    "steps": [
      "Criar um plano de estudos de 5 dias, dividindo os principais tópicos da Revolução Francesa (Causas, Fases, Consequências).",
      "Para cada dia, sugerir um tópico específico e uma atividade (ex: leitura, assistir a um vídeo, responder a perguntas).",
      "Gerar um resumo conciso (máximo 500 palavras) sobre a Revolução Francesa, destacando os eventos e personagens principais.",
      "No final, criar 3 perguntas de múltipla escolha sobre o tema para autoavaliação."
    ],
    "output_format": "Documento de texto com duas seções: 'Plano de Estudos' e 'Resumo do Tópico'."
  },
  "constraints": [
    "A linguagem deve ser clara e didática.",
    "O resumo deve ser imparcial e focado nos fatos históricos.",
    "As perguntas devem cobrir diferentes aspectos do resumo."
  ],
  "user_input": "Tenho uma prova sobre a Revolução Francesa na próxima semana."
}
```

---

## 3. Prompt Estruturado (KERNEL)

- **K (Keep it simple):** Criar um plano de estudos e um resumo sobre a Revolução Francesa.
- **E (Easy to verify):** O resultado deve conter um plano de 5 dias, um resumo de até 500 palavras e 3 perguntas de múltipla escolha.
- **R (Reproducible results):** O conteúdo histórico é factual e não muda.
- **N (Narrow scope):** A tarefa está focada em um único tópico histórico.
- **E (Explicit constraints):** Resumo com no máximo 500 palavras, linguagem didática.
- **L (Logical structure):**

    1.  **Task:** Gerar um plano de estudos semanal e um resumo sobre a Revolução Francesa.
    2.  **Input:** Prova de história sobre a Revolução Francesa.
    3.  **Constraints:** Resumo limitado a 500 palavras. Linguagem clara. Incluir 3 perguntas de teste.
    4.  **Output:** Documento com as seções 'Plano de Estudos' e 'Resumo do Tópico'.
    5.  **Verify:** Verificar a estrutura do plano, a contagem de palavras do resumo e a presença das 3 perguntas.
