# PROMPTS PARA ASSISTENTE DE MARKETING MÉDICO

---

## 1. Prompt Genérico

Faça o marketing da minha clínica.

---

## 2. Prompt Estruturado (JSON)

```json
{
  "task": "criar_campanha_de_marketing_medico",
  "context": {
    "background": "Uma clínica de dermatologia quer atrair mais pacientes para um novo tratamento de rejuvenescimento facial.",
    "user_goal": "Desenvolver uma campanha de marketing digital de 30 dias para promover o novo tratamento."
  },
  "instructions": {
    "steps": [
      "Definir o público-alvo (ex: mulheres, 40-60 anos, interessadas em estética).",
      "Criar um cronograma de conteúdo para 4 semanas, com 2 posts por semana para Instagram e Facebook.",
      "Sugerir temas para os posts (ex: 'Benefícios do tratamento', 'Antes e Depois', 'Perguntas e Respostas').",
      "Escrever o texto para o primeiro post do Instagram, incluindo uma chamada para 'agendar uma avaliação'.",
      "Sugerir uma ideia para um anúncio pago no Facebook (ex: vídeo curto com um especialista explicando o procedimento)."
    ],
    "output_format": "Documento de planejamento de campanha com seções para cada item."
  },
  "constraints": [
    "Toda a comunicação deve seguir as diretrizes de publicidade do Conselho Federal de Medicina (CFM).",
    "Evitar linguagem que prometa resultados garantidos.",
    "O tom deve ser informativo, profissional e ético."
  ],
  "user_input": "Novo tratamento: 'Lifting a Laser XYZ'. Clínica focada em tecnologia de ponta."
}
```

---

## 3. Prompt Estruturado (KERNEL)

- **K (Keep it simple):** Criar um plano de campanha de marketing digital para um novo tratamento dermatológico.
- **E (Easy to verify):** O plano deve conter público-alvo, cronograma de 4 semanas, temas de posts, a copy do primeiro post e uma ideia de anúncio.
- **R (Reproducible results):** A estrutura da campanha pode ser replicada para outros tratamentos.
- **N (Narrow scope):** A tarefa foca no planejamento da campanha para um único serviço.
- **E (Explicit constraints):** Seguir as regras do CFM. Não prometer resultados. Tom profissional.
- **L (Logical structure):**

    1.  **Task:** Desenvolver uma campanha de marketing digital de 30 dias para um tratamento dermatológico.
    2.  **Input:** Clínica de dermatologia, novo tratamento 'Lifting a Laser XYZ'.
    3.  **Constraints:** Conformidade com as normas do CFM. Tom ético e informativo.
    4.  **Output:** Documento de planejamento de campanha detalhado.
    5.  **Verify:** Checar se todos os 5 componentes da campanha foram entregues e se as restrições éticas foram consideradas.
