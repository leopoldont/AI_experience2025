# PROMPTS PARA ASSISTENTE DE BRANDING

---

## 1. Prompt Genérico

Crie um branding para minha empresa.

---

## 2. Prompt Estruturado (JSON)

```json
{
  "task": "gerar_identidade_de_marca",
  "context": {
    "background": "Estamos lançando uma nova marca de cafés especiais focada em sustentabilidade e grãos de origem única.",
    "user_goal": "Desenvolver uma identidade de marca completa, incluindo nome, slogan, missão, visão e valores."
  },
  "instructions": {
    "steps": [
      "Gerar 5 sugestões de nomes para a marca.",
      "Criar 3 opções de slogans.",
      "Definir uma declaração de missão e visão.",
      "Listar 5 valores fundamentais da marca.",
      "Sugerir um perfil de público-alvo."
    ],
    "output_format": "Um documento de texto estruturado com seções para cada item."
  },
  "constraints": [
    "Evitar nomes que já existam no mercado de cafés.",
    "O tom da comunicação deve ser sofisticado e consciente."
  ],
  "user_input": "A empresa se chama 'Café Fictício' e o diferencial é o processo de torra artesanal."
}
```

---

## 3. Prompt Estruturado (KERNEL)

- **K (Keep it simple):** Gerar os elementos centrais de identidade para uma nova marca de café.
- **E (Easy to verify):** O resultado deve conter 5 nomes, 3 slogans, missão, visão, 5 valores e a definição do público-alvo.
- **R (Reproducible results):** O prompt não contém informações que mudam com o tempo.
- **N (Narrow scope):** A tarefa é focada exclusivamente na criação da identidade da marca.
- **E (Explicit constraints):** Não usar nomes de marcas de café existentes. O tom deve ser sofisticado.
- **L (Logical structure):**

    1.  **Task:** Gerar a identidade da marca para uma nova empresa de cafés especiais.
    2.  **Input:** Foco em sustentabilidade, grãos de origem única e torra artesanal.
    3.  **Constraints:** Evitar nomes de marcas de café existentes. Manter um tom de voz sofisticado e consciente.
    4.  **Output:** Documento de texto com seções para: Nomes (5), Slogans (3), Missão, Visão, Valores (5) e Público-alvo.
    5.  **Verify:** Verificar se todos os 6 itens solicitados foram entregues no formato especificado.
